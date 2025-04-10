from django.contrib.auth.models import User
from django.test import TestCase
from .models import Ad, ExchangeProposal
from django.urls import reverse


class AdModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.ad = Ad.objects.create(
            user=self.user,
            title='Книга',
            description='Хорошая книга',
            category='Книги',
            condition='new'
        )

    def test_ad_creation(self):
        self.assertEqual(self.ad.title, 'Книга')
        self.assertEqual(self.ad.user.username, 'testuser')
        self.assertIsNotNone(self.ad.created_at)

    def test_ad_edit_by_author(self):
        self.ad.title = 'Изменённый заголовок'
        self.ad.save()
        self.assertEqual(Ad.objects.get(id=self.ad.id).title, 'Изменённый заголовок')


class ExchangeProposalTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')

        self.ad1 = Ad.objects.create(
            user=self.user1,
            title='Ноутбук',
            description='Старый ноут',
            category='Электроника',
            condition='used'
        )

        self.ad2 = Ad.objects.create(
            user=self.user2,
            title='Гитара',
            description='Акустическая',
            category='Музыка',
            condition='new'
        )

        self.proposal = ExchangeProposal.objects.create(
            ad_sender=self.ad1,
            ad_receiver=self.ad2,
            comment='Обменяемся?',
        )

    def test_proposal_creation(self):
        self.assertEqual(self.proposal.status, 'pending')
        self.assertEqual(self.proposal.comment, 'Обменяемся?')
        self.assertEqual(self.proposal.ad_sender.title, 'Ноутбук')

    def test_proposal_status_change(self):
        self.proposal.status = 'accepted'
        self.proposal.save()
        self.assertEqual(ExchangeProposal.objects.get(id=self.proposal.id).status, 'accepted')


class AdFunctionalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass')
        self.other_user = User.objects.create_user(username='not_author', password='pass')

        self.ad = Ad.objects.create(
            user=self.user,
            title='Велосипед',
            description='Почти новый',
            category='Транспорт',
            condition='used'
        )

    def test_delete_ad_by_author(self):
        self.client.login(username='author', password='pass')
        response = self.client.post(reverse('ad_delete', args=[self.ad.id]))
        self.assertEqual(response.status_code, 302)  # редирект после удаления
        self.assertFalse(Ad.objects.filter(id=self.ad.id).exists())

    def test_delete_ad_by_not_author(self):
        self.client.login(username='not_author', password='pass')
        response = self.client.post(reverse('ad_delete', args=[self.ad.id]))
        self.assertEqual(response.status_code, 403)  # доступ запрещён
        self.assertTrue(Ad.objects.filter(id=self.ad.id).exists())

    def test_search_ads(self):
        Ad.objects.create(
            user=self.user,
            title='Самокат',
            description='Электро самокат',
            category='Транспорт',
            condition='new'
        )
        response = self.client.get(reverse('ad_list'), {'search': 'самокат'})
        self.assertContains(response, 'Самокат')
        self.assertNotContains(response, 'Велосипед')

    def test_filter_ads_by_category_and_condition(self):
        Ad.objects.create(
            user=self.user,
            title='Планшет',
            description='Для работы',
            category='Электроника',
            condition='new'
        )
        response = self.client.get(reverse('ad_list'), {'category': 'Электроника', 'condition': 'new'})
        self.assertContains(response, 'Планшет')
        self.assertNotContains(response, 'Велосипед')


