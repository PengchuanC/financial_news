from django.db import models

# Create your models here.

class News(models.Model):
    infopubldate = models.DateField(verbose_name='新闻发布日期')
    infopubltime = models.CharField(verbose_name='新闻发布时间', null=True, max_length=8)
    media = models.CharField(verbose_name='媒体出处', null=True, max_length=50)
    newscategory = models.CharField(verbose_name='新闻栏目', max_length=200, null=True)
    infotitle = models.CharField(verbose_name='新闻标题', max_length=200)
    infoshorttitle = models.CharField(verbose_name='新闻副标题', max_length=200, null=True)
    abstract = models.TextField(verbose_name='新闻摘要', null=True)
    content = models.TextField(verbose_name='新闻内容')
    author = models.CharField(verbose_name='撰写作者', max_length=200, null=True)
    linkaddress = models.CharField(verbose_name='链接地址', max_length=300, null=True)
    category = models.CharField(verbose_name='栏目分类', max_length=50)
    infolevel = models.IntegerField(verbose_name='信息级别')
    
    class Meta:
        db_table = 'news_newsinfo'
        verbose_name = '新闻资讯表'
        verbose_name_plural = verbose_name
