import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do CSV
data = pd.read_csv('./ecommerce_sales_analysis.csv')

# Cálculo das vendas totais
data['total_sales'] = data.filter(like='sales_month_').sum(axis=1)

# Produtos com maior receita total
top_products = data[['product_name', 'total_sales']].sort_values(by='total_sales', ascending=False)
print("\nProdutos com Maior Receita Total:")
print(top_products.head())

# Gráfico de produtos com maior receita total
plt.figure(figsize=(12, 6))
sns.barplot(x='total_sales', y='product_name', data=top_products.head(10), palette='viridis')
plt.title('Produtos com Maior Receita Total')
plt.xlabel('Total de Vendas')
plt.ylabel('Produto')
plt.tight_layout()
plt.show()

# Total de vendas por categoria
category_sales = data.groupby('category')['total_sales'].sum().sort_values(ascending=False)
print("\nTotal de Vendas por Categoria:")
print(category_sales)

# Gráfico de total de vendas por categoria
plt.figure(figsize=(12, 6))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='viridis')
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Produtos mais vendidos por categoria
top_selling_per_category = data.groupby('category').apply(
    lambda x: x.loc[x['total_sales'].idxmax(), 'product_name']
).reset_index(name='Top_Selling_Product')
print("\nProdutos Mais Vendidos por Categoria:")
print(top_selling_per_category)

# Gráfico dos produtos mais vendidos por categoria
plt.figure(figsize=(12, 8))
top_selling_per_category_sorted = top_selling_per_category.merge(
    data[['product_name', 'category', 'total_sales']],
    left_on=['category', 'Top_Selling_Product'],
    right_on=['category', 'product_name']
)
sns.barplot(
    x='total_sales', 
    y='Top_Selling_Product', 
    hue='category', 
    data=top_selling_per_category_sorted, 
    palette='viridis'
)
plt.title('Produtos Mais Vendidos por Categoria')
plt.xlabel('Total de Vendas')
plt.ylabel('Produto')
plt.legend(title='Categoria')
plt.tight_layout()
plt.show()
