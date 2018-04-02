class Person:
    def __init__(self,name):
        #姓名
        self.name = name
        #血量
        self.blood = 100
    #给弹夹安装子弹
    def installBullet(self,clip,bullet):
        #弹夹放置子弹
        clip.saveBullet(bullet)
    #安装弹夹
    def installClip(self,gun,clip):
        #给枪安装弹夹
        gun.mountingClip(clip)
    #拿枪
    def takeGun(self,gun):
        self.gun = gun
    #开火
    def fire(self,enemy):
        self.gun.shoot(enemy)
    #显示person
    def __str__(self):
        return self.name + "剩余血量：" + str(self.blood)
    #掉血
    def loseBlood(self,damage):
        self.blood -= damage
class Clip:
    def __init__(self,capacity):
        self.capacity = capacity
        self.currentList = []
    #安装子弹
    def saveBullet(self,bullet):
        #判断子弹是否装满
        if len(self.currentList) < self.capacity:
            self.currentList.append(bullet)
    #显示弹夹信息
    def __str__(self):
        return "弹夹当前的数量为：" + str(len(self.currentList))+"/"+str(self.capacity)
    #射出子弹
    def shotBullet(self):
        #判断是否有子弹
        if len(self.currentList) > 0:
            #子弹减1
            self.currentList.pop()
            return bullet
        else:
            return None
class Bullet:
    def __init__(self,damage):
        self.damage = damage
    #子弹伤害方法
    def hurt(self,enemy):
        enemy.loseBlood(self.damage)
    pass
class Gun:
    def __init__(self):
        self.clip = None
    def __str__(self):
        if self.clip:
            return "枪有弹夹"
        else:
            return "枪没有弹夹"
    #子弹连接弹夹
    def mountingClip(self,clip):
        if not self.clip:
            self.clip = clip
    #射击
    def shoot(self,enemy):
        bullet = self.clip.shotBullet()
        if bullet:
            bullet.hurt(enemy)
        else:
            print("没有子弹了，放了空枪。。。")
soldier = Person("老王")
clip = Clip(20)
print(clip)
i = 0
#装子弹
while i<5:
    bullet = Bullet(5)
    soldier.installBullet(clip,bullet)
    i  += 1
print(clip)
gun = Gun()
print(gun)
soldier.installClip(gun,clip)
print(gun)
enemy = Person("敌人")
print(enemy)
soldier.takeGun(gun)
soldier.fire(enemy)
print(clip)
print(enemy)
soldier.fire(enemy)
print(clip)
print(enemy)