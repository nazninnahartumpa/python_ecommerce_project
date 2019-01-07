from django.shortcuts import render

from .models import Cart

# Create your views here.
#Just show only if the session is running then card is exist otherwise showing Create new cart Id
# def cart_home(request):
# 	cart_id = request.session.get('cart_id', None)
# 	if cart_id is None:
# 		print("Create new cart ID")
# 		request.session['cart_id'] = 12 #If user is logout then after login by this line session id will be created.
# 	else:
# 		print("Cart ID is exists")

# 	return render(request, "carts/carts_home.html", {})

# By this code session id object will be created in the Cart model of admin panal.We can see the id in the admin panal.
# def cart_home(request):
# 	cart_id = request.session.get('cart_id', None)
# 	if cart_id is None:
# 		cart_obj = Cart.objects.create(user=None)
# 		request.session['cart_id'] = cart_obj.id
# 		print("New cart created !")
# 	else:
# 		print("Cart ID is exists")
# 		print(cart_id)
# 		cart_obj = Cart.objects.get(id=cart_id)

# 	return render(request, "carts/carts_home.html", {})



#Create session id by the model manager with the user associated.
# def cart_create(request):
# 	cart_obj = Cart.objects.create(user=None)
# 	print("New cart created")
# 	return cart_obj

# def cart_home(request):
# 	cart_id = request.session.get('cart_id', None)
# 	qs = Cart.objects.filter(id=cart_id)
# 	if qs.count() == 1:
# 		print('Cart ID exist')
# 		cart_obj = qs.first()
# 		if request.user.is_authenticated and cart_obj.user is None:
# 			cart_obj.user = request.user
# 			cart_obj.save()
# 	else:
# 		cart_obj = Cart.objects.new(user=request.user)
# 		request.session['cart_id'] = cart_obj.id
# 	return render(request, "carts/carts_home.html", {})


#all code are gone to the model
def cart_home(request):
	cart_obj = Cart.objects.new_or_get(request)
	
	return render(request, "carts/carts_home.html", {})