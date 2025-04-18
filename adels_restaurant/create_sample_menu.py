import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adels_restaurant_project.settings')
django.setup()

from menu.models import Category, MenuItem

def create_sample_menu():
    # Delete existing data
    Category.objects.all().delete()
    MenuItem.objects.all().delete()
    
    # Create categories
    appetizers = Category.objects.create(
        name='Appetizers',
        description='Start your meal with our delicious appetizers.'
    )
    
    main_courses = Category.objects.create(
        name='Main Courses',
        description='Enjoy our chef\'s special main courses.'
    )
    
    desserts = Category.objects.create(
        name='Desserts',
        description='Finish your meal with our sweet treats.'
    )
    
    drinks = Category.objects.create(
        name='Drinks',
        description='Refresh yourself with our selection of beverages.'
    )
    
    # Create menu items - Appetizers
    MenuItem.objects.create(
        name='Bruschetta',
        description='Toasted bread topped with diced tomatoes, fresh basil, garlic, and olive oil.',
        price=8.99,
        category=appetizers
    )
    
    MenuItem.objects.create(
        name='Calamari',
        description='Crispy fried calamari served with marinara sauce and lemon wedges.',
        price=12.99,
        category=appetizers
    )
    
    MenuItem.objects.create(
        name='Mozzarella Sticks',
        description='Breaded mozzarella sticks fried until golden brown, served with marinara sauce.',
        price=9.99,
        category=appetizers
    )
    
    # Create menu items - Main Courses
    MenuItem.objects.create(
        name='Grilled Salmon',
        description='Fresh salmon fillet grilled to perfection, served with seasonal vegetables and lemon butter sauce.',
        price=24.99,
        category=main_courses
    )
    
    MenuItem.objects.create(
        name='Beef Tenderloin',
        description='8oz beef tenderloin cooked to your preference, served with mashed potatoes and grilled asparagus.',
        price=29.99,
        category=main_courses
    )
    
    MenuItem.objects.create(
        name='Chicken Alfredo',
        description='Fettuccine pasta tossed in creamy Alfredo sauce with grilled chicken breast and parmesan cheese.',
        price=18.99,
        category=main_courses
    )
    
    MenuItem.objects.create(
        name='Vegetable Risotto',
        description='Creamy Arborio rice cooked with seasonal vegetables, white wine, and parmesan cheese.',
        price=16.99,
        category=main_courses
    )
    
    # Create menu items - Desserts
    MenuItem.objects.create(
        name='Tiramisu',
        description='Classic Italian dessert made with layers of coffee-soaked ladyfingers and mascarpone cream.',
        price=8.99,
        category=desserts
    )
    
    MenuItem.objects.create(
        name='Chocolate Lava Cake',
        description='Warm chocolate cake with a molten chocolate center, served with vanilla ice cream.',
        price=9.99,
        category=desserts
    )
    
    MenuItem.objects.create(
        name='Cheesecake',
        description='New York style cheesecake with a graham cracker crust, topped with fresh berries.',
        price=8.99,
        category=desserts
    )
    
    # Create menu items - Drinks
    MenuItem.objects.create(
        name='House Wine',
        description='Glass of our house red or white wine.',
        price=7.99,
        category=drinks
    )
    
    MenuItem.objects.create(
        name='Craft Beer',
        description='Selection of local craft beers.',
        price=6.99,
        category=drinks
    )
    
    MenuItem.objects.create(
        name='Signature Cocktail',
        description='Our bartender\'s special creation using premium spirits and fresh ingredients.',
        price=12.99,
        category=drinks
    )
    
    MenuItem.objects.create(
        name='Fresh Juice',
        description='Freshly squeezed orange, apple, or carrot juice.',
        price=4.99,
        category=drinks
    )
    
    print('Sample menu created successfully!')

if __name__ == '__main__':
    create_sample_menu()

