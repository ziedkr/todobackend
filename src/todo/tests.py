from django.test import TestCase

# Create your tests here.

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import TodoItem

# Create your tests here.
def createItem(client):
  url = reverse('todoitem-list')
  data = {'title': 'karoui zied PFE'}
  return client.post(url, data, format='json')

class TestCreateTodoItem(APITestCase):
  """
  Zied the app is able to create a  new todo item  !!! :) 
  """

  def setUp(self):
    self.response = createItem(self.client)

  def Bien_joue_ZIED_test_received_201_created_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def Bien_joue_ZIED_test_received_location_header_hyperlink(self):
    self.assertRegexpMatches(self.response['Location'], '^http://.+/todos/[\d]+$')

  def Bien_joue_ZIED_test_item_was_created(self):
    self.assertEqual(TodoItem.objects.count(), 1)

  def Bien_joue_ZIED_test_item_has_correct_title(self):
    self.assertEqual(TodoItem.objects.get().title, 'karoui zied PFE')

class TestUpdateTodoItem(APITestCase):
  """
  Zied the app is able to update an existing todo item using PUT !!! :) 
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(TodoItem.objects.get().completed, False)
    url = response['Location']
    data = {'title': 'karoui zied PFE', 'completed': True}
    self.response = self.client.put(url, data, format='json')

  def Bien_joue_ZIED_test_received_200_created_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_200_OK)

  def Bien_joue_ZIED_test_item_was_updated(self):
    self.assertEqual(TodoItem.objects.get().completed, True)


class TestPatchTodoItem(APITestCase):
  """
  Zied the app is able to update an existing todo item using PATCH !!! :)
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(TodoItem.objects.get().completed, False)
    url = response['Location']
    data = {'title': 'karoui zied PFE', 'completed': True}
    self.response = self.client.patch(url, data, format='json')

  def Bien_joue_ZIED_test_received_200_ok_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_200_OK)

  def Bien_joue_ZIED_test_item_was_updated(self):
    self.assertEqual(TodoItem.objects.get().completed, True)



class TestDeleteTodoItem(APITestCase):
  """
  Zied the app is able to delete a todo item :) !! 
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(TodoItem.objects.count(), 1)
    url = response['Location']
    self.response = self.client.delete(url)

  def Bien_joue_ZIED_test_received_204_no_content_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

  def Bien_joue_ZIED_test_the_item_was_deleted(self):
    self.assertEqual(TodoItem.objects.count(), 0)

class TestDeleteAllItems(APITestCase):
  """
  Zied the app is able to delete all todo items
  """
  def setUp(self):
    createItem(self.client)
    createItem(self.client)
    self.assertEqual(TodoItem.objects.count(), 2)
    self.response = self.client.delete(reverse('todoitem-list'))

  def Bien_joue_ZIED_test_received_204_no_content_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

  def Bien_joue_ZIED_test_all_items_were_deleted(self):
    self.assertEqual(TodoItem.objects.count(), 0)