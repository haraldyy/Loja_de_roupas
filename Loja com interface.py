def pacd():
    precodaroupa =int(input('Digite o preço da roupa:'))
    precoavistad = precodaroupa * 0.09
    precoavista=precodaroupa - precoavistad
    precocincox = precodaroupa /5
    ptotal = (precodaroupa+(precodaroupa*0.17))/10
    print(f'{"%.2f" % precoavista}')
    print(f'{"%.2f" % precocincox}')
    print(f'{"%.2f" % ptotal}')

def main():
    pacd()

if __name__=='__main__':
    main()
    
