from ClanBattleRecorder import Recorder

if __name__ == '__main__':
    recorder = Recorder()
    bosses = {
        1: [1000, 2000, 3000, 4000, 5000],
        2: [1000, 2000, 3000, 4000, 5000],
        3: [1000, 2000, 3000, 4000, 5000],
        4: [1400, 2000, 3000, 4000, 5000],
        5: [1000, 2000, 3000, 4000, 5000],
    }
    #kmr 为普通用户，rmk 为管理用户
    recorder.setBossHP(bosses, 'rmk') #设置 boss 血量
    recorder.dayStarts() #定时运行，新的一天开始，刀数清零
    recorder.getBossStatus('kmr') #查询当前血量，返回字典，值为 tuple(周目数, 血量)
    recorder.getPlayerStatus('rmk') #查刀，返回包含所有玩家情况的字典，值为 tuple(已出刀数, 剩余补时数)
    recorder.addPlayer('baka', 1, 'rmk') #添加普通玩家 baka
    recorder.enterBattle('kmr', 3) #进入战斗
    recorder.cancelBattle('kmr') #我不进了
    recorder.reportDamage(3, 'kmr', True, 23333) #报刀，参数为：boss, 玩家, 是否为完整刀, 伤害

