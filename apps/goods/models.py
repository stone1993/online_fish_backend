#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
from datetime import datetime
from django.db import  models
from DjangoUeditor.models import UEditorField

class GoodsCategory(models.Model):
    """
    商品类型
    """
    CATEGORY_TYPE =  {
        (1, "一级目录"),
        (2, "二级目录"),
        (3, "三级目录")
    }
    name = models.CharField(default="",max_length=30,verbose_name="类别名",help_text="类别名")
    code = models.CharField(default="",max_length=30,verbose_name="类别编号",help_text="类别编号")
    desc = models.TextField(default="",verbose_name="类别描述",help_text="类别描述")
    category_type = models.IntegerField(default=1,choices=CATEGORY_TYPE,verbose_name="类型级别",help_text="类型级别")
    parent_category =models.ForeignKey('self',null=True,blank=True,verbose_name="父类类型",help_text="父类类型",related_name="sub_cat")
    is_tab = models.BooleanField(default=False,verbose_name="是否导航",help_text="是否导航")
    add_time  = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name

class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, related_name="brands",verbose_name="商品类型", help_text="商品类型")
    name = models.CharField(default="",max_length=30,verbose_name="品牌名",help_text=u"品牌名")
    desc = models.TextField(default="",max_length=200,verbose_name="品牌描述",help_text="品牌描述")
    image = models.ImageField(max_length=200,upload_to="brands/")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory,null=True,blank=True,verbose_name="商品类型",help_text="商品类型")
    good_sn = models.CharField(max_length=30,default="",verbose_name="商品编号",help_text="商品编号")
    name = models.CharField(max_length=300,verbose_name="商品名称")
    click_num = models.IntegerField(default=0,verbose_name="商品点击量")
    sold_num =  models.IntegerField(default=0,verbose_name="商品销售量",help_text="商品销售量")
    fav_num = models.IntegerField(default=0,verbose_name="商品收藏量")
    goods_num = models.IntegerField(default=0,verbose_name="库存量")
    market_price = models.FloatField(default=0,verbose_name="市场价格")
    shop_price = models.FloatField(default=0,verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500,verbose_name="商品简介")
    goods_desc = UEditorField(verbose_name=u'内容',imagePath="goods/image",width=1000,height=300,
                              filePath="goods/file/",default='')
    ship_free = models.BooleanField(default=True,verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images",null=True,blank=True,verbose_name="封面图")
    is_new = models.BooleanField(default=False,verbose_name="是否新品")
    is_hot = models.BooleanField(default=False,verbose_name="是否热销",help_text="是否热销")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods,verbose_name="商品",related_name="images")
    image = models.ImageField(upload_to="",verbose_name="图片",null=True,blank=True)
    image_url = models.CharField(max_length=300,null=True,blank=True,verbose_name="图片Url")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.goods.name



class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods,verbose_name="轮播的商品")
    image = models.ImageField(upload_to="banner",verbose_name="轮播图")
    index = models.IntegerField(default=0,verbose_name="轮播顺序")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

class IndexAd(models.Model):
    category =models.ForeignKey(GoodsCategory,related_name="category",verbose_name="商品类目")
    goods = models.ForeignKey(Goods,related_name="goods")
    class Meta:
        verbose_name = "首页商品类别广告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name