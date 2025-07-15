
def remove_duplicates(list1:list,list2=list):
        list1_removed_duplicates=[]
        list2_removed_duplicates=[]
        for i in list1:
            if i not in list1_removed_duplicates:
                list1_removed_duplicates.append(i)
        for j in list2:
            if j not in list2_removed_duplicates:
                list2_removed_duplicates.append(j)
        return list1_removed_duplicates,list2_removed_duplicates
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            list_s=list(s)
            list_t=list(t)
            list_s_after_remove_duplicates,list_r_after_remove_duplicates=remove_duplicates(list_s,list_t)
            print(list_s_after_remove_duplicates)
            print(list_r_after_remove_duplicates)
            num=0
            for i in range(len(list_s_after_remove_duplicates)):
                for j in list_r_after_remove_duplicates:
                    if list_s_after_remove_duplicates[i]==j:
                        num+=1
            if num == len(list_r_after_remove_duplicates) or num == len(list_s_after_remove_duplicates):
                return True
            else:
                return False
                         
sol = Solution()
s=input("Enter the string s:")
t=input("Enter the string t:")
print(sol.isAnagram(s,t))