from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.

products_items = [
    {
        'id': 1,
        'name': 'Smartphone',
        'description': 'Latest model smartphone with AMOLED display and 5G support.',
        'price': 8500,
        'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9'
    },
    {
        'id': 2,
        'name': 'Laptop',
        'description': 'Lightweight laptop with Intel i7, 16GB RAM, and 512GB SSD.',
        'price': 21500,
        'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8'
    },
    {
        'id': 3,
        'name': 'Wireless Headphones',
        'description': 'Noise-cancelling over-ear headphones with Bluetooth 5.2.',
        'price': 3200,
        'image': 'https://images.unsplash.com/photo-1580894908361-967195033215'
    },
    {
        'id': 4,
        'name': 'Smartwatch',
        'description': 'Water-resistant smartwatch with health tracking features.',
        'price': 2600,
        'image': 'https://images.unsplash.com/photo-1603791440384-56cd371ee9a7'
    },
    {
        'id': 5,
        'name': 'Gaming Console',
        'description': 'Next-gen gaming console with 4K support and 1TB storage.',
        'price': 12500,
        'image': 'https://images.unsplash.com/photo-1606813909227-0df4e16f6029'
    },
    {
        'id': 6,
        'name': 'Bluetooth Speaker',
        'description': 'Portable Bluetooth speaker with deep bass and 10-hour battery.',
        'price': 1200,
        'image': 'https://images.unsplash.com/photo-1585386959984-a4155224a1b3'
    },
    {
        'id': 7,
        'name': 'Tablet',
        'description': '10-inch tablet with stylus support and 128GB storage.',
        'price': 7800,
        'image': 'https://images.unsplash.com/photo-1588776814546-ec8a87f1f561'
    },
    {
        'id': 8,
        'name': 'Camera',
        'description': 'Mirrorless digital camera with 24MP sensor and 4K video.',
        'price': 14500,
        'image': 'https://images.unsplash.com/photo-1519183071298-a2962eadcdb2'
    },
    {
        'id': 9,
        'name': 'External Hard Drive',
        'description': '2TB USB 3.0 external hard drive for backup and storage.',
        'price': 950,
        'image': 'https://images.unsplash.com/photo-1587202372775-e7b84b1f2d91'
    },
    {
        'id': 10,
        'name': 'Wireless Mouse',
        'description': 'Ergonomic wireless mouse with programmable buttons.',
        'price': 450,
        'image': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3'
    }
]

def products(request):
    return render(request,'index.html', context={'products':products_items})

def product_details(request, id):
    try:
        product = next((p for p in products_items if p['id'] == id), None)
        if product is None:
            raise Http404("Product not found")
        return render(request, 'product_detail.html', context={'product': product})
    except:
        raise Http404("Product not found")