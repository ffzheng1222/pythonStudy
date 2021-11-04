from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_created=True)

    def __str__(self):
        """返回表示模式的字符串"""
        return self.text


class Enter(models.Model):
    """学习到的某个主题具体的信息"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Mete:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."
