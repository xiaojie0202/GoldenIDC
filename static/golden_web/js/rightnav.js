$(function(){
	$(".header01 .nav1 li").hover(function(){
	    $(this).find(".nav2").stop(true).slideToggle(); 
	 });
	 //fullnav
	 var qcloud='';
	$('.header01 .nav1 .product, .header03').hover(function(){
		var that=$(".header03");
		clearTimeout(qcloud);
		qcloud = setTimeout(function(){
		$(that).stop(true,true).fadeIn(200);
		}, 150);
		$('.header01 .nav1 .product a').addClass('cur');
	},function(){
		var that=$(".header03");
		clearTimeout(qcloud);
		qcloud = setTimeout(function(){
//		$('.header02 .nav .product, .header03').removeClass('active');
		$(that).stop(true,true).fadeOut(200);
		}, 150);
		$('.header01 .nav1 .product a').removeClass('cur');
	});
	 
	//点击展开隐藏导航
 $('.navbar-btn').click(function(){
    $('.mobile-nav').addClass('is-visible');
    $('.cd-overlay').addClass('is-visible');
 });
 $('.mobile-nav .close').click(function(){
    $('.mobile-nav').removeClass('is-visible');
    $('.cd-overlay').removeClass('is-visible');
 });
 $('.dropdown > li > a').click(function(){
 	$(this).closest('li').siblings().find('.nav2').slideUp();
    $(this).next('.nav2').slideToggle();
 });
})