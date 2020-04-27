# Generated by Django 2.1.4 on 2020-04-27 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addressee',
            fields=[
                ('addressee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='收件人id')),
                ('addressee_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='收件人姓名')),
                ('addressee_tel', models.IntegerField(blank=True, null=True, verbose_name='收件人手机号')),
                ('addressee_site', models.CharField(blank=True, max_length=256, null=True, verbose_name='地址')),
                ('addressee_tag', models.CharField(blank=True, max_length=32, null=True, verbose_name='标签')),
                ('addressee_state', models.IntegerField(blank=True, choices=[(0, '默认收货地址'), (None, None)], null=True, verbose_name='是否为默认，0默认')),
                ('addressee_created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '收件信息',
                'verbose_name_plural': '收件信息',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('commodity_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='商品id')),
                ('commodity_created_time', models.DateTimeField(auto_now_add=True, verbose_name='商品创建的时间')),
                ('commodity_state_putaway', models.IntegerField(choices=[(0, '正在审核'), (1, '未上架'), (2, '已上架'), (3, '违规商品'), (4, '已删除')], default=0, verbose_name='商品的上架状态')),
                ('commodity_state_recommend', models.IntegerField(blank=True, choices=[(0, '热卖推荐'), (1, '新品推荐'), (2, '季节推荐')], null=True, verbose_name='商品的推荐状态')),
                ('commodity_cover', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品主要的封面图')),
                ('commodity_mc_video', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品介绍视频')),
                ('commodity_video_cover', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品介绍视频的封面图')),
                ('commodity_price_bazaar', models.IntegerField(blank=True, null=True, verbose_name='商品市场价')),
                ('commodity_price_vip', models.IntegerField(blank=True, null=True, verbose_name='商品vip价格')),
                ('commodity_price_svip', models.IntegerField(blank=True, null=True, verbose_name='商品svip价格')),
                ('commodity_price_agency', models.IntegerField(blank=True, null=True, verbose_name='商品代理价格')),
                ('commodity_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='商品的标题')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='CommodityComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='评论id')),
                ('comment_appraise', models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')], verbose_name='商品评价')),
                ('comment_content', models.CharField(blank=True, max_length=256, null=True, verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('CommentToCommodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontEnd.Commodity', verbose_name='商品di,多对一')),
            ],
            options={
                'verbose_name': '商品图片详情',
                'verbose_name_plural': '商品图片详情',
            },
        ),
        migrations.CreateModel(
            name='CommodityImgDescribe',
            fields=[
                ('img_describe_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='描述图片id')),
                ('img_describe_url', models.CharField(max_length=128, verbose_name='描述图片链接')),
                ('img_describe_created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('ImgDescribeToCommodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontEnd.Commodity', verbose_name='商品di,多对一')),
            ],
            options={
                'verbose_name': '商品图片描述',
                'verbose_name_plural': '商品图片描述',
            },
        ),
        migrations.CreateModel(
            name='CommodityImgDetails',
            fields=[
                ('img_details_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='详情图片id')),
                ('img_details_url', models.CharField(max_length=128, verbose_name='描述图片链接')),
                ('img_details_created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('ImgDetailsToCommodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontEnd.Commodity', verbose_name='商品di,多对一')),
            ],
            options={
                'verbose_name': '商品图片详情',
                'verbose_name_plural': '商品图片详情',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单id')),
                ('order_number', models.IntegerField(verbose_name='订单编号')),
                ('order_state', models.IntegerField(choices=[(0, '未支付'), (1, '已支付'), (2, '已发货'), (3, '已到货'), (4, '已签收'), (5, '已完成')], default=0, verbose_name='订单状态')),
                ('order_serial_number', models.IntegerField(verbose_name='交易流水号')),
                ('OrderToAddressee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frontEnd.Addressee', verbose_name='购物使用的收货地址id')),
                ('OrderToCommodity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frontEnd.Commodity', verbose_name='购买的商品id')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCar',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='购物车id')),
                ('car_number', models.IntegerField(default=1, verbose_name='加入购物车的数量')),
                ('car_created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加到购物车的时间')),
                ('CarToCommodity', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='frontEnd.Commodity', verbose_name='商品id,多对多，购物车中的对象与商品对象的关系')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='用户id')),
                ('user_name', models.CharField(max_length=18, unique=True, verbose_name='用户名')),
                ('user_password', models.CharField(max_length=128, verbose_name='密码')),
                ('user_pay_password', models.IntegerField(blank=True, null=True, verbose_name='支付密码')),
                ('user_nickname', models.CharField(blank=True, max_length=18, null=True, verbose_name='用户昵称')),
                ('user_sex', models.IntegerField(blank=True, choices=[(None, None), (0, '女'), (1, '男')], default=None, null=True, verbose_name='性别')),
                ('user_created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_registration_date', models.DateTimeField(auto_now_add=True, verbose_name='最近一次登陆时间')),
                ('user_portrait', models.ImageField(blank=True, null=True, upload_to='', verbose_name='头像')),
                ('user_tel', models.IntegerField(blank=True, null=True, verbose_name='手机号')),
                ('user_vip_class', models.IntegerField(choices=[(0, '普通VIP'), (1, '至尊VIP'), (2, '代理商')], default=0, verbose_name='vip等级')),
                ('user_status', models.IntegerField(choices=[(0, '从未下单的'), (1, '下单未支付的'), (2, '下过单的')], default=0, verbose_name='用户质量')),
                ('user_balance', models.IntegerField(default=0, verbose_name='账户余额')),
            ],
            options={
                'verbose_name': '账号信息',
                'verbose_name_plural': '账号信息',
            },
        ),
        migrations.AddField(
            model_name='shoppingcar',
            name='CarToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontEnd.User', verbose_name='用户id,多对一，多个购物车中的商品对应一个用户'),
        ),
        migrations.AddField(
            model_name='order',
            name='OrderToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frontEnd.User', verbose_name='下单用户id'),
        ),
        migrations.AddField(
            model_name='commoditycomment',
            name='CommentToOrder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frontEnd.Order', verbose_name='订单di,多对一'),
        ),
        migrations.AddField(
            model_name='commoditycomment',
            name='CommentToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frontEnd.User', verbose_name='进行评论的用户id'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='CommodityToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontEnd.User', verbose_name='发布商品用户的ID'),
        ),
        migrations.AddField(
            model_name='addressee',
            name='AddresseeToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frontEnd.User', verbose_name='多对一，多个Addressee对应一个User'),
        ),
    ]
