from django.db import models

# Create your models here

class CurrencyType(models.Model):
    title = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=3)

    def __str__(self):
        return self.abbreviation

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

# Wallet/Account - one of your money storage (cash or non-cash)
class MoneyAccount(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False) #Name
    currency = models.ForeignKey(CurrencyType, on_delete=models.CASCADE)
    is_cash = models.BooleanField(default=False) #Flag - cash or non-cash

    def __str__(self):
        return f"{self.title, self.currency }"

    class Meta:
        verbose_name = "Wallet(Account)"
        verbose_name_plural = "Wallets(Accounts)"

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class FinOperation(models.Model):
    wallet_account = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE)
    op_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_expanses = models.BooleanField(default=True) #Flag - expanses or income
    date_created = models.DateField(auto_now_add=True)
    sum = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Financial Operation"
        verbose_name_plural = "Financial Operations"

    def __str__(self):
        return f"{self.wallet_account.title}: {self.op_category.category_name} - {self.sum}"
