#截至2023.7.2
'''matrixutil致力于尽可能有教学内容的计算和表达线性代数问题(写的很粗糙,后面我也许会考虑重写)'''

#备注,numpy数组的第一个标是第几行,第二个标是第几列,别给我整什么花活.shape也是这样取值的
#(凭感觉)考虑到浮点数的问题,求Ax=b的解的时候可以考虑使用最小二乘解numpy.linalg.lstsq替代(同时numpy.linalg.solve不能解超定方程)
#以下函数未经过浮点数这类问题的测试,这是值得注意的(可能之后要限定精度)
#精度问题很多
#尚未使用isinstance判断输入的类型(待办事项),各种健全性有待加强

#调用必要的库
import numpy as np

#所有函数出现Error和Exception时会返回Python中的虚数1j作为标识,以便其他程序对Error和Exception的情况进行判断检测

#必要的前置准备

#自定义 Exception类
class MatrixException(Exception):
    '''自定义矩阵运算报错MatrixException'''
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
#向量投影计算(合格)
def project(a:np.ndarray,b:np.ndarray):
    '''该函数实现了向量a在向量b方向上的投影(b!=0)'''
    x=np.copy(a)
    y=np.copy(b)
    length2=np.dot(y,y)
    try:
        if length2==0:
            raise MatrixException("投影方向为0")
        length1=np.dot(x,y)
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    except ValueError:
        print("输入的向量维度不一致")
        return 1j
    else:
        return length1/length2 
#多项式环乘法在Python上的实现(合格)
def mulmul(a:list,b:list):
    '''a和b均以列表的形式输入即可,其次数递减排列,最后一个数对应的次数为0,并以相同的规则返回计算得到的多项式'''
    try:
        la=len(a)
        lb=len(b)
        if la*lb==0:
            raise MatrixException("多项式输入格式有误")
    except MatrixException as e:
        print(e.value)
        return 1j
    except TypeError:
        print("多项式输入格式有误")
        return 1j
    else:
        result=[0 for i in range(0,la+lb-1)]
        for i in range(0,la):
            for j in range(0,lb):
                result[i+j]+=a[i]*b[j]
        return result
    
#初等行列变换函数系列(合格)                   
def r_swap(matrix:np.ndarray,i:int,j:int,express=True):
    '''这个函数对输入的矩阵的第i行和第j行进行初等行变换,第一行视作i=1'''
    output=np.copy(matrix)
    try:
        dimension=output.shape[0]
        if i>dimension or i<1 or j>dimension or j<1:
            raise MatrixException("超出尺寸")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    except IndexError:
        print("matrix输入有误")
        return 1j
    else:
        temp=np.array(output[i-1])
        output[i-1]=output[j-1]
        output[j-1]=temp
        if (express):
            print("矩阵的第"+str(round(i,4))+"行和第"+str(round(j,4))+"行进行互换")
        return output
def c_swap(matrix:np.ndarray,i:int,j:int,express=True):
    '''这个函数对输入的矩阵的第i列和第j列进行初等列变换,第一列视作i=1'''
    output=np.copy(matrix)
    output=output.T
    try:
        dimension=output.shape[0]
        if i>dimension or i<1 or j>dimension or j<1:
            raise MatrixException("超出尺寸")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    except IndexError:
        print("matrix输入有误")
        return 1j
    else:
        temp=np.array(output[i-1])
        output[i-1]=output[j-1]
        output[j-1]=temp
        if (express):
            print("矩阵的第"+str(round(i,4))+"列和第"+str(round(j,4))+"列进行互换")
        return output.T
def r_multiple(matrix:np.ndarray,i:int,times:int,express=True):
    '''这个函数对输入的矩阵的第i行作times倍进行初等行变换,第一行视作i=1'''
    output=np.copy(matrix)
    try:
        dimension=output.shape[0]
        if i>dimension or i<1:
            raise MatrixException("超出尺寸")
        if times==0:
            raise MatrixException("数乘为0")
    except MatrixException as e:
            print("矩阵运算出现了不合法的情况: "+e.value)
            return 1j
    except IndexError:
        print("matrix输入有误")
        return 1j
    else:
        output[i-1]=output[i-1]*times
        if (express):
            print("矩阵的第"+str(round(i,4))+"行数乘"+str(round(times,4))+"倍")
        return output    
def c_multiple(matrix:np.ndarray,i:int,times:int,express=True):
    '''这个函数对输入的矩阵的第i列作times倍进行初等列变换,第一列视作i=1'''
    output=np.copy(matrix)
    output=output.T
    try:
        dimension=output.shape[0]
        if i>dimension or i<1:
            raise MatrixException("超出尺寸")
        if times==0:
            raise MatrixException("数乘为0")
    except MatrixException as e:
            print("矩阵运算出现了不合法的情况: "+e.value)
            return 1j
    except IndexError:
        print("matrix输入有误")
        return 1j
    else:
        output[i-1]=output[i-1]*times
        if (express):
            print("矩阵的第"+str(round(i,4))+"列数乘"+str(round(times,4))+"倍")
        return output.T    
def r_plus(matrix:np.ndarray,i:int,j:int,times:int,express=True):
    '''这个函数将输入的矩阵的第j行的times倍加到第i行上进行初等行变换,第一行视作i=1'''
    output=np.copy(matrix)
    try:
        dimension=output.shape[0]
        if i>dimension or i<1 or j>dimension or j<1:
            raise MatrixException("超出尺寸")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    except IndexError:
        print("matrix输入有误")
        return 1j
    else:
        output[i-1]=output[i-1]+output[j-1]*times
        if (express):
            print("矩阵的第"+str(round(i,4))+"行加上了第"+str(round(j,4))+"行的"+str(round(times,4))+"倍")
        return output
def c_plus(matrix:np.ndarray,i:int,j:int,times:int,express=True):
    '''这个函数将输入的矩阵的第j列的times倍加到第i列上进行初等列变换,第一列视作i=1'''
    output=np.copy(matrix)
    output=output.T
    try:
        dimension=output.shape[0]
        if i>dimension or i<1 or j>dimension or j<1:
            raise MatrixException("超出尺寸")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    except IndexError:
        print("matrix输入有误")
        return 1j
    else:
        output[i-1]=output[i-1]+output[j-1]*times
        if (express):
            print("矩阵的第"+str(round(i,4))+"列加上了第"+str(round(j,4))+"列的"+str(round(times,4))+"倍")
        return output.T       
#高斯消元法类函数系列(合格)
def r_steps(matrix:np.ndarray,express=True):
    '''这个函数将输入的矩阵使用高斯消元法变成行阶梯形矩阵(不是简化阶梯形)'''
    output=np.copy(matrix)
    dimension=output.shape
    i=0
    j=0
    if len(dimension)!=2:
        print("输入matrix格式有误")
        return 1j
    else:
        while(i<dimension[0] and j<dimension[1]):
            if output[i,j]==0:
                for k in range(i+1,dimension[0]):
                    if output[k,j]!=0:
                        output=r_swap(output,i+1,k+1,express)
                        output=[round(i,6) for i in output[k]]
                        break
                if output[i,j]==0:
                    j+=1
            else:
                for k in range(i+1,dimension[0]):
                    if output[k,j]!=0:
                        output=r_plus(output,k+1,i+1,-(output[k,j]+.0)/output[i,j],express)
                        output[k]=[round(i,4) for i in output[k]]
                i+=1
                j+=1
        return output
def c_steps(matrix:np.ndarray,express=True):
    '''这个函数将输入的矩阵使用高斯消元法变成列阶梯形矩阵(不是简化阶梯形)'''
    output=np.copy(matrix)
    dimension=output.shape
    i=0
    j=0
    if len(dimension)!=2:
        print("输入matrix格式有误")
        return 1j
    else:
        while(i<dimension[0] and j<dimension[1]):
            if output[i,j]==0:
                for k in range(j+1,dimension[1]):
                    if output[i,k]!=0:
                        output=c_swap(output,j+1,k+1,express)
                        break
                if output[i,j]==0:
                    i+=1
            else:
                for k in range(j+1,dimension[1]):
                    if output[i,k]!=0:
                        output=c_plus(output,k+1,j+1,-(output[i,k]+.0)/output[i,j],express)
                        output[:,k]=[round(i,4) for i in output[:,k]]
                i+=1
                j+=1
        return output
def r_simpsteps(matrix:np.ndarray,express=True):
    '''这个函数将输入的矩阵使用高斯消元法变成行最简形阶梯形矩阵'''
    output=r_steps(matrix,express)
    try:
        output==1j
    except ValueError:
        return 1j
    else:
        i=0
        dimension=output.shape
        for i in range(0,dimension[0]):
            for j in range(0,dimension[1]):
                if output[i,j]!=0:
                    output=r_multiple(output,i+1,1./output[i,j],express)
                    output[i]=[round(j,4) for j in output[i]]
                    for k in range(0,i):
                        if output[k,j]!=0:
                            output=r_plus(output,k+1,i+1,-output[k,j],express)
                            output[k,j]=0
                            output[k]=[round(i,4) for i in output[k]]
                    break
        return output
def c_simpsteps(matrix:np.ndarray,express=True):
    '''这个函数将输入的矩阵使用高斯消元法变成列最简形阶梯形矩阵'''
    output=c_steps(matrix)
    try:
        output==1j
    except ValueError:
        return 1j
    else:
        i=0
        dimension=output.shape
        for i in range(0,dimension[1]):
            for j in range(0,dimension[0]):
                if output[j,i]!=0:
                    output=c_multiple(output,i+1,1./output[j,i],express)
                    output[:,i]=[round(j,4) for j in output[:,i]]
                    for k in range(0,i):
                        if output[j,k]!=0:
                            output=c_plus(output,k+1,i+1,-output[j,k],express)
                            output[:,k]=[round(i,4) for i in output[:,k]]
                    break
        return output 
#行列式计算(合格)
def guassian(matrix:np.ndarray,express=False):
    '''该函数使用了高斯消元法求解行列式'''
    ma=np.copy(matrix)
    dimension=ma.shape
    try:
        if len(dimension)!=2:
                raise MatrixException("不是矩阵")
        else:
            if dimension[0]!=dimension[1]:
                raise MatrixException("不是方阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        output=1
        ma=r_steps(ma,express)
        for i in np.diagonal(ma):
            output*=i
        return str(round(output,4))
#计算逆矩阵(合格)
def inverse(matrix:np.ndarray,express=False):
    '''该函数使用了初等变换法计算输入矩阵的逆矩阵'''
    output=np.copy(matrix)
    dimension=output.shape
    try:
        if len(dimension)!=2:
                raise MatrixException("不是矩阵")
        else:
            if dimension[0]!=dimension[1]:
                raise MatrixException("不是方阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        temp=np.zeros((dimension[0],dimension[1]))
        for k in range(0,dimension[0]):
            temp[k,k]=1
        output=np.concatenate((output,temp),axis=1)
        output=r_simpsteps(output,express)
        a=output[:,:dimension[0]]
    try:
        temp=1
        for i in np.diagonal(a):
            temp*=i
        if i==0:
            raise MatrixException("奇异矩阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        output=output[:,dimension[0]:]             
        return output
#LU分解(合格)
def lu(matrix:np.ndarray,express=False):
    '''该函数使用初等变换法实现了LU分解(不允许行变换的Doolittle分解)的具体过程'''
    u=np.copy(matrix)
    dimension=u.shape
    try:
        if len(dimension)!=2:
                raise MatrixException("不是矩阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        l=np.zeros((dimension[0],dimension[0]))
        i=0
        j=0
        error=0
        while(i<dimension[1] and j<dimension[0]):
            if u[j,i]==0 and max(u[j:,i])!=0:
                error=1
                break
            else:
                if u[j,i]==0:
                    i+=1
                else:
                    l[j:,j]=u[j:,i]
                    for k in range(j+1,dimension[0]):
                        if u[i,k]!=0:
                            plus=-(u[k,i]+.0)/u[j,i]
                            u=r_plus(u,k+1,j+1,plus,express)
                            u[k]=[round(i,4) for i in u[k]]            
                    l[:,j]=l[:,j]/l[j,j]
                    i+=1
                    j+=1
    try:
        if error==1:
            raise MatrixException("出现了行交换")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        return (l,u)
#LDU分解(合格)
def ldu(matrix:np.ndarray,express=False):
    '''该函数基于之前的LU分解,实现了LDU分解(只基于方阵和|A|!=0的情况)'''
    u=np.copy(matrix)
    dimension=u.shape
    try:
        if dimension[0]!=dimension[1]:
            raise MatrixException("不是方阵")
        else:
            if np.linalg.det(u)==0:
                raise MatrixException("|A|为0")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        (l,u)=lu(u,express)
        d=np.diag(np.diag(u))
        for i in range(0,dimension[0]):
            u[i,:]/=u[i,i]
            u[i]=[round(j,4) for j in u[i]]  
        return (l,d,u)
#Crout分解(未验证)
def crout(matrix:np.ndarray,express=False):
    '''该函数基于之前的LDU分解,实现了Crout分解(只基于方阵和|A|!=0的情况)'''
    u=np.copy(matrix)
    (l,d,u)=ldu(u,express)
    l=np.dot(l,d)
    return (l,u)        
#QR分解(合格)
def qr(matrix:np.ndarray):
    '''直接使用了numpy下的qr分解,但进行了Exception的修饰,返回了(Q,R)'''
    ma=np.copy(matrix)
    dimension=ma.shape
    try:
        if len(dimension)!=2:
            raise MatrixException("不是矩阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        return np.linalg.qr(ma)    
#取子矩阵(合格)
def son_true(matrix:np.ndarray,chosen:list):
    '''该函数只能使用二维列表chosen进行按[i]行、[j]列对矩阵进行选取,第1行记作i=1'''
    dimension=np.shape(matrix)
    try:
        if len(dimension)!=2:
                raise MatrixException("不是矩阵")
        else:
            if min(chosen[0])<1 or max(chosen[0])>dimension[0] or min(chosen[1])<1 or max(chosen[1])>dimension[1]:
                raise MatrixException("超出尺寸")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        output=np.zeros((len(chosen[0]),len(chosen[1])))
        x=0
        for i in chosen[0]:
            y=0
            for j in chosen[1]:
                output[x,y]=matrix[i-1,j-1]
                y+=1
            x+=1    
        return output
def son_false(matrix:np.ndarray,chosen:list):
    '''该函数只能使用二维列表chosen进行排除[i]行、[j]列对矩阵进行选取,第1行记作i=1'''
    dimension=np.shape(matrix)
    try:
        if len(dimension)!=2:
                raise MatrixException("不是矩阵")
        else:    
            if min(chosen[0])<1 or max(chosen[0])>dimension[0] or min(chosen[1])<1 or max(chosen[1])>dimension[1]:
                raise MatrixException("超出尺寸")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        output=np.zeros((dimension[0]-len(chosen[0]),dimension[1]-len(chosen[1])))
        x=0
        for i in range(0,dimension[0]):
            y=0
            for j in range(0,dimension[1]):
                if i+1 not in chosen[0] and j+1 not in chosen[1]:
                    output[x,y]=matrix[i,j]
                    y+=1
            if i+1 not in chosen[0]:
                x+=1    
        return output        
#求伴随矩阵(合格)
def adjoint(matrix:np.ndarray,express=False):
    '''该函数实现了计算输入矩阵的伴随矩阵'''
    ma=np.copy(matrix)
    dimension=ma.shape
    try:
        if dimension[0]!=dimension[1]:
            raise MatrixException("不是方阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        r=np.linalg.matrix_rank(ma)
        if r==dimension[0]:
            output=np.linalg.inv(ma)*np.linalg.det(ma)
            if express:
                print("矩阵的秩为n,其伴随矩阵A*=|A|A^(-1)")
        elif r==dimension[0]-1:
            output=np.zeros(dimension)
            for i in range(0,dimension[0]):
                for j in range(0,dimension[1]):
                    output[i,j]=np.linalg.det(son_false(ma,[[j+1],[i+1]]))
            if express:
                print("该矩阵的秩为n-1,其伴随矩阵有R(A*)=1")
        else:
            output=np.zeros(dimension)
            if express:
                print("该矩阵的秩为n-2,其伴随矩阵A*=0")
        return output
#Schmidt正交化过程(合格)
def schmidt(matrix:np.ndarray,express=False):
    '''该函数取输入的列满秩矩阵的列向量按照顺序进行Schmidt正交化过程(不进行标准化)并以与原矩阵相同的格式返回.
    当express=True时以矩阵形式
    [1 * *]
    [0 1 *]
    [0 0 1]
    返回计算过程的参数表'''
    ma=np.copy(matrix)
    dimension=ma.shape
    try:
        if np.linalg.matrix_rank(ma)!=dimension[1]:
            raise MatrixException("非列满秩矩阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        col=[]
        result=[]
        if express:
            parameter=np.zeros((dimension[1],dimension[1]))
            for i in range(0,dimension[1]):
                parameter[i,i]=1
        for i in range(0,dimension[1]):
            col.append(ma[:,i])
        result.append(col[0])
        for j in range(1,dimension[1]):
            reduce=np.zeros(dimension[0])
            for k in range(0,j):
                reduce-=project(col[j],result[k])*result[k]
                if express:
                    parameter[k,j]=-project(col[j],result[k])
            result.append(col[j]+reduce)
        m=np.zeros((dimension[0],dimension[1]))
        for i in range(0,dimension[1]):
            m[:,i]=result[i]
        if express:
            return (m,parameter)
        else:
            return m
#求特征值的函数包装(合格)---------------------------------->有关eigvals和eig函数的区别有待考察,本函数尚未实现求特征向量
def eigvals(matrix:np.ndarray,absolute=False):
    '''该函数用于对某个矩阵求特征值(包括重根,取小数后6位)并按递减顺序返回(当absolute=True时按照绝对值递减顺序返回)'''
    ma=np.copy(matrix)
    dimension=ma.shape
    try:
        if dimension[0]!=dimension[1]:
            raise MatrixException("不是方阵")
        if len(dimension)!=2:
            raise MatrixException("不是矩阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况:"+e.value)
        return 1j
    else:
        eigvals=np.linalg.eigvals(ma)
        numlist=eigvals.tolist()
        if absolute:
            numlist.sort(key=lambda x:abs(x),reverse=True)
        else:
            numlist.sort(reverse=True)
        numlist=[complex(round(i.real,6),round(i.imag,6)) for i in numlist]#在此处确定保留的小数位数
        eigvals=np.array(numlist)
        return eigvals
#求某个矩阵对应的特征多项式(合格)
def eigmul(matrix:np.ndarray,expand=False):
    '''该函数基于(偷懒)eigvals函数(该函数计算方式不同于直接计算特征多项式,故为保精度保留2位小数,也不能出现复数情况)
    用于对某个矩阵求特征多项式(当expand=True时返回展开形式的多项式)并以string的形式返回'''
    e=eigvals(matrix)
    if e.all()==1j:
        return 1j
    else:
        string=""
        if expand:
            multi=[[1,-i] for i in e]
            result=multi[0]
            for i in range(1,len(multi)):
                result=mulmul(result,multi[i])
            lr=len(result)
            for i in range(0,lr):
                num=round(result[i],2)#取保留小数位数
                if abs(num)!=1 or i==lr-1:
                    s1=str(num)
                else:
                    s1=""
                if i==lr-2:
                    s2=""
                if i<lr-2:
                    s2=str(lr-1-i)    
                if i==0:
                    if num!=0:
                        string+=s1+"λ"+s2
                elif i<lr-1:
                    if num>0:
                        string+="+"+s1+"λ"+s2
                    if num<0:
                        string+=s1+"λ"+s2
                else:
                    if num>0:
                        string+="+"+s1
                    if num<0:
                        string+=s1
        else:    
            i=0
            while i<len(e):
                lam=e[i]
                n=1
                for j in range(i+1,len(e)):
                    if e[j]==lam:
                        n+=1
                    else:
                        break
                if lam>0:
                    string+="(λ-"+str(lam)+")"
                elif lam<0:
                    string+="(λ+"+str(-lam)+")"
                else:
                    string+="λ"
                if n>1:
                    string+=str(n)        
                i=i+1
        return string      
#求线性表出的系矩阵(即解AX=B,B为一般的矩阵)-------------------(未检验且很可能有浮点数问题)
def li_express(A:np.ndarray,B:np.ndarray):
    ma1=np.copy(A)
    ma2=np.copy(B)
    error=0
    dimension1=ma1.shape
    dimension2=ma2.shape
    r=np.linalg.matrix_rank(ma1)
    try:
        if dimension1[0]!=dimension2[0]:
            raise MatrixException("列向量维度不一致")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        X=np.zeros((dimension1[1],dimension2[1]))
        for i in range(0,dimension2[1]):
            if r<np.linalg.matrix_rank(np.concatenate((ma1,ma2[i]),axis=1)):
                error=1
                break
            else:
                X[:,i]=np.linalg.solve(ma1,ma2[:,i])
        if error==1:
            print("B的列向量不能被A的列向量线性表出")
        else:
            return X
#一般情形下的最小二乘法求Ax=b的近似解过程(法方程AtAx=Atb)实现函数(未验证)
def my_lstsq(matrix:np.ndarray,express=False,error=False):
    '''matrix为Ax=b的增广矩阵,express=True时将会一同返回中间量(x,AtA,Atb)而不是单纯返回结果(x),
    当A不是列满秩时返回x为高斯消元后的结果(此时最小二乘解不唯一)当A列满秩且error=True时会返回计算误差e'''
    ma=np.copy(matrix)
    dimension=ma.shape
    try:
        if len(dimension)!=2:
            raise MatrixException("不是矩阵")
        if dimension[1]==1:
            raise MatrixException("不是增广矩阵")
    except MatrixException as e:
        print("矩阵运算出现了不合法的情况: "+e.value)
        return 1j
    else:
        A=ma[:,:-1]
        B=ma[:,-1]
        r=np.linalg.matrix_rank(A)
        if r==dimension[1]-1:
            a=np.dot(A.T,A)
            b=np.dot(A.T,B)
            x=np.linalg.solve(a,b)
            if error:
                e=euclid(x,b)
        else:
            G=np.concatenate((a,b),axis=1)
            x=r_simpsteps(G,express=False)
        result=[x]
        if express:
            result.append(a)
            result.append(b)
        if r==dimension[1]-1:
            result.append(e)
        return result
#取矩阵的某一极大线性无关列向量组的函数(未验证)
def c_maxlninde(matrix:np.ndarray,express=False):
    '''该函数用于求矩阵中列下标最小的一组极大线性无关向量组'''
    ma=np.copy(matrix)
    dimension=ma.shape
    A=r_steps(ma,express)
    num=[]
    for i in range(0,dimension[0]):
        for j in range(0,dimension[1]):
            if ma[i,j]!=0:
                num.append(j)
                break
    return [ma[:,k] for k in num]
#鉴于本人学艺不精,思维枯竭了,下列尝试整理有关书中涉及的空间几何问题的快捷函数(其实很容易被替代就是了)
def euclid(a:list,b:list):
    '''该函数用于求a,b两向量的欧式范数结果'''
    try:
        if len(a)!=len(b):
            raise MatrixException("长度不一致")
    except MatrixException as e:
        print("运算出现了不合法的情况: "+e.value)
        return 1j
    except TypeError:
        print("运算出现了不合法的情况: 输入错误")
        return 1j
    else:
        return (sum((a-b)**2 for a,b in zip(a,b)))**.5

#中期展示函数
def display(matrix:np.ndarray):
    '''该函数用于中期答辩时展示数学运算'''
    ma=np.copy(matrix)
    switch={'rs':r_steps,'cs':c_steps,'srs':r_simpsteps,'scs':c_simpsteps,'gas':guassian,\
            'inv':inverse,'lu':lu,'ldu':ldu,'crt':crout,'qr':qr,'adj':adjoint,'smt':schmidt,\
            'egv':eigvals,'egm':eigmul,}
    s='m'
    while(s!='q'):
        i=False
        while (s=='m'):
            print("输入c以退出菜单界面选择函数,输入q以退出整个展示,输入其他字符以浏览菜单")    
            if (not i):
                print("高斯消元法变为行阶梯形矩阵:rs")
                print("高斯消元法变为列阶梯形矩阵:cs")
                print("高斯消元法变成行最简形阶梯形矩阵:srs")
                print("高斯消元法变成列最简形阶梯形矩阵:scs")
                print("高斯消元法求解行列式:gas")
                print("初等变换法计算输入矩阵的逆矩阵:inv")
                print("使用初等变换法实现了LU分解:lu")
            if (i):
                print("使用初等变换法实现了LDU分解:ldu")
                print("使用初等变换法实现了Crout分解:crt")
                print("实现了QR分解:qr")
                print("计算输入矩阵的伴随矩阵:adj")
                print("Schmidt正交化过程:smt")
                print("对某个矩阵求特征值:egv")
                print("求某个矩阵对应的特征多项式:egm")
            s=input("输入操作符:")
            if (s!='q' and s!='c'):
                s='m'
            i=not i
        while(s=='c'):
            print("输入m以退出选择界面进入菜单,输入q以退出整个展示,输入其他字符以选择功能函数")
            s=input("输入操作符:")
            if (s in switch.keys()):
                try:
                    switch.get(s)(ma,express=False)
                except TypeError:
                    if (s=='egv'):
                        re=eigvals(ma,(input("输入y按照绝对值大小排序特征值:")=='y'))
                    elif (s=='egm'):
                        re=eigmul(ma,(input("输入y以输出多项式的展开式:")=='y'))
                    else:
                        re=switch.get(s)(ma)
                else:
                    re=switch.get(s)(ma,(input("输入y以展示过程:")=='y'))
                if (input("输入y以查看最终结果")=='y'):
                    print(re)
            if (s!='q' and s!='m'):
                s='c'
    print("结束展示")


#防止matrixutil被单独使用
if '__name__'=='__main__':
    pass           