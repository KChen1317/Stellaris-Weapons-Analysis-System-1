######### Stellaris Weapon Stats Analysis System #########
#########                  V.1.                  #########

import random

def main():
    banner()
    prompt_start()
    end="false"
    while end!="quit":
        temp=set_up()
        iterations=input("How many times do you want to run the simulation?\nThe recommended amount is 1000.\n----->")
        output=sim_loop(temp[0],temp[1],int(iterations))
        print("\n\n\nThe average time is "+str(output[1])+" over "+str(iterations)+".")
        see_list="no"
        see_list=input("Do you wish to see the input?\nENTER yes to do so\nelse enter any other input\n----->")
        if see_list=="yes":
            print("The data list is:\n"+str(output))
        end=input("Do you wish to stop the program?\nenter quit to terminate this program\nENTER any other input to continue")
    quit()
        


def banner():
    print("######### Stellaris Weapon Stats Analysis System ######### \n#########                  V.1.                  #########")
    print("\n\n                   Created By Kevin Chen")
    print("\n\n\n\n")



def prompt_start():
    bypass="off"
    display_license="off"
    print("Welcome to the SWSAS V.1")
    display_license=input("\n\nThis code is released under a open source license. View?(yes/no)\n--->")     #### TO DO####
    if display_license=="yes":
        license_display()
    bypass=input("If you wish to skip the explanation of how to use this system\nenter bypass(only do if you are familiar with this version)\nELSE enter any other input\n----->")
    if bypass!="bypass":
        tutorial()


        
def license_display():              ####MIT license####
    print("Copyright 2019 Kevin Chen\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ""Software""), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\nTHE SOFTWARE IS PROVIDED ""AS IS"", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
    print("\n\n\n")
####find a way to get his to not be so long... and apply to all strings here####
    



def tutorial():                                     ####Only runs at first execution(to the program's view )####
    print("This program is intended to help the user analyse weapons in game.")
    print("It takes data for both a target and a weapon and runs multiple Monte-Carlo simulations to generate a report.")
    print("This program DOES NOT include in it's caculation:\nranges\nspeeds\nRoF\npoint defence(where applicable)")
    print("The program WILL require stats for both the simuated target and weapons.")
    print("Please note that this program can not handle incorrect data types and may crash if said data is entered.")
    data_entry_guide()




def data_entry_guide():                             ####Instructs user on data entry####
    display_examples_="no"      ##### WARNING this is diferent from the function display_examples() #####
    print("The target hull, armor,and shield data must be entered as Positive Intergers.")
    print("After enetering said data, one can choose to include target regeneration.\nQuick internet research indicates that this does not appear to happen unless target is not attacked for some amount of time.")
    print("If one chooses to, one must also include all related data as Positive Numbers.")
    print("Weapon min and max damage must be provided as Positive Numbers.")
    print("All weapon bonuses must be in Decimal form. \nIf the weapon bypasses a defence completely (eg. disruptors) set the weapon bonus to Zero.")
    print("Weapon penetration/bypass must be in Decimal form.")
    print("Weapon accurancy and tracking must be entered as Decimals.")
    display_examples_=input("Do you wish to see examples?\nIf so ENTER yes\nelse enter any other input\n--->")
    if display_examples_=="yes":
        display_examples()



def display_examples():                             ####Displays example data####
    print("--Small Railgun (T3 vanilla)--")
    print("Min dmg:8 Max dmg:27 \nHull bonus:0\nArmor pen:0 Armor bonus:-0.5\nShield pen:0 Shield bonus:0.5\nAccurancy:0.75 Tracking:0.5")
    print("--Ripper Autocannon (T2 vanilla)--")
    print("Min dmg:10 Max dmg:21 \nHull bonus:0.25\nArmor pen:0 Armor bonus:-0.75\nShield pen:0 Shield bonus:0.5\nAccurancy:0.85 Tracking:0.75")
    print("--Small Disruptor (T1 vanilla)--")
    print("Min dmg:1 Max dmg:18 \nHull bonus:0\nArmor pen:1 Armor bonus:0\nShield pen:0 Shield bonus:0\nAccurancy:1 Tracking:0.6")
    print("--Enigmatic Energy Autocannon (Leviathan based modded)--")
    print("Min dmg:25 Max dmg:35 \nHull bonus:0.25\nArmor pen:0.5 Armor bonus:-0.5\nShield pen:0 Shield bonus:1\nAccurancy:0.9 Tracking:0.65")
    print("--Model target (all stats maxed)--")
    print("Hull:23320 Armor:13320 Shield:19008\n Hull regen:12 Armor regen:16 Shield regen:172.8\nEvasion:0.9")
    print("--Model target (one shot)--")
    print("Hull:1 Armor:0 Shield:0\n Hull regen:0 Armor regen:0 Shield regen:0\nEvasion:0")



def set_up():
    target_hull=0           ####var init for data####
    target_armor=0      
    target_shield=0
    enable_regen_calc="no"
    target_hull_regen=0     ####var init for damage reducing factors####
    target_armor_regen=0
    target_shield_regen=0
    target_evasion=0
    weapon_min_dmg=0        ####start of weapon data####
    weapon_max_dmg=0
    weapon_hull_bonus=0
    weapon_armor_pen=0
    weapon_armor_bonus=0
    weapon_shield_pen=0
    weapon_shield_bonus=0
    weapon_accurancy=0      ####data about weapon lock on####
    weapon_tracking=0
    input_complete="no"
    target_data=1
    weapon_data=1
    print("----Set up has started----")
    
    while(input_complete!="correct"):                    ####loops until data entry is confirmed####
        target_hull=input("target hull? --->")
        target_armor=input("target armor? --->")
        target_shield=input("target shield? --->")
        enable_regen_calc=input("enable regen calc? ---->")
        if enable_regen_calc=="yes":
            enable_regen_calc=True
            print("regen calculations enabled")
            target_hull_regen=input("hull regen?--->")    
            target_armor_regen=input("armor regen?--->")
            target_shield_regen=input("shield regen?--->")
        else:
            enable_regen_calc=False
        target_evasion=input("target evasion?--->")
        weapon_min_dmg=input("weapon min damage?--->")        
        weapon_max_dmg=input("weapon max damage?--->")
        weapon_hull_bonus=input("weapon hull bonus?--->")
        weapon_armor_pen=input("weapon armor pen?--->")
        weapon_armor_bonus=input("weapon armor bonus?--->")
        weapon_shield_pen=input("weapon shield pen?--->")
        weapon_shield_bonus=input("weapon shield bonus?--->")
        weapon_accurancy=input("weapon accurancy?--->")      
        weapon_tracking=input("weapon tracking?--->")
        input_error="none"                                ####tracks the prescenc of errors####
        try:
            target_data={"hull":int(target_hull),"armor":int(target_armor),"shield":int(target_shield),"regen on":enable_regen_calc,"hull regen":float(target_hull_regen),"armor regen":float(target_armor_regen),"shield regen":float(target_shield_regen),"evasion":float(target_evasion)}
            weapon_data={"min dmg":int(weapon_min_dmg),"max dmg":int(weapon_max_dmg),"hull bonus":float(weapon_hull_bonus),"armor pen":float(weapon_armor_pen),"armor bonus":float(weapon_armor_bonus),"shield pen":float(weapon_shield_pen),"shield bonus":float(weapon_shield_bonus),"accurancy":float(weapon_accurancy),"tracking":float(weapon_tracking)}
        except:
            input_error="found"
        if input_error!="found":
            print("check the following weapon and target stats")            ####if the data does not have errors, verify input####
            print("Target data\n"+str(target_data))
            print("Weapon data\n"+str(weapon_data))
            input_complete=input("If the data diplayed is correct\nEnter correct\nelse enter any other input\n----->")
        else:
            show_help="no"
            print("One of the inputs are not in the right data type.")
            show_help=input("Do you want to go over the data input requirement?\nENTER yes if so\nelse enter any other input\n-----> ")
            if show_help=="yes":
                data_entry_guide()   
    return(target_data,weapon_data)
        


def sim_loop(target_data,weapon_data,iterations):
    print("\n\n\n\n\n------Entering loop------")
    data_list=[]
    avg=0
    temp_iterate=iterations
    while temp_iterate!=0:
        print("Starting iteration"+str(temp_iterate))
        temp=sim(target_data,weapon_data)
        data_list.append(temp)
        temp_iterate=temp_iterate-1
    print("\n\n\n"+str(iterations)+"iterations finished.")
    print("-----Performing final caculations.-----")
    if data_list[0]=="infinite":    ####handles when the weapon would never hit####
        return(data_list,"infinite")
    else:
        print(str(temp))
        avg=sum(data_list)/iterations
        return(data_list,avg)



def sim(target_data,weapon_data):
    hit_chance=max(0,weapon_data["accurancy"]-max(0,target_data["evasion"]-weapon_data["tracking"]))
    sh_pen=weapon_data["shield pen"]
    sh_bonus=1+weapon_data["shield bonus"]
    arm_pen=weapon_data["armor pen"]
    arm_bonus=1+weapon_data["armor bonus"]
    hull_bonus=1+weapon_data["hull bonus"]
    min_dmg=weapon_data["min dmg"]
    max_dmg=weapon_data["max dmg"]
    init_hull=target_data["hull"]
    init_arm=target_data["armor"]
    init_sh=target_data["shield"]
    calc_regen=target_data["regen on"]
    hull_regen=target_data["hull regen"]
    arm_regen=target_data["armor regen"]
    sh_regen=target_data["shield regen"]
    hull=init_hull              ####these variables are created before the loop is started####
    arm=init_arm
    sh=init_sh
    attack_attempts="infinite"
    if hit_chance==0:           ####since the weapon will never hit####
        return(attack_attempts) #### function will terminate early####
    else:
        attack_attempts=0
    while hull>=0.009:           ####due to floats, this sort of comparison is needed####
        if calc_hit(hit_chance)=="hit":         ####roll for hit chance####    
            atk=dmg(min_dmg,max_dmg)
            attack_attempts=attack_attempts+1
            if sh>=0.009:                  ###shield layer###
                temp=dmg_calc(sh,atk,sh_pen,sh_bonus,"sh")
                if temp[0]<=0.009:         ####use to calc pass through ptential (same for armor layer as well)####
                    atk=temp[1]                 ####calc pass through####
                    sh=0
                else:
                    sh=temp[0]                  ####calc shield reduction####
                    atk=temp[1]
                                                ####else the shield is already gone####
                                                ####so we should move on to the next layer####
            if arm>=0.009:                 ###armor layer###
                temp=dmg_calc(arm,atk,arm_pen,arm_bonus,"arm")
                if temp[0]<=0.009:
                    atk=temp[1]                 ####calc pass through####
                    arm=0
                else:
                    arm=temp[0]                 ####calc arm reduction####
                    atk=temp[1]
                                                ####else the arm is already gone####
                                                ####so we should move on to the next layer####
            if hull>=0.009:                ###hull layer###
                temp=dmg_calc(hull,atk,0,hull_bonus,"hull")
                if temp[0]<=0.009:
                    hull=0                      ####killed or over kill so do nothig####
                else:
                    hull=temp[0]
            else:
                do_nothing()
        if hull<=0.009:     ####check hull, if hull is probably 0, exit and return)####
            break
        if calc_regen=="regen on":   #### if the target passes the death check(eg. still alive) and regen is caculated, add after dmg calc####
            hull=hull+hull_regen
            arm=arm+arm_regen
            sh=sh+sh_regen
    return(attack_attempts)



def calc_hit(chance):
    roll=random.randint(0,100)/100
    if abs(chance)<=abs(roll+0.001) or abs(chance)<=abs(roll-0.001):        #### due to floats, this comparison is used####
        return("hit")                                                       ####with a 0.001 margin on both sides####
    else:
        return("not hit")



def dmg(min_dmg,max_dmg):
    dmg=random.randint(min_dmg,max_dmg)
    return(dmg)



def dmg_calc(hp,dmg,pen,bonus,dmg_type):            #### function cals dmg and remaining layer health####
    if type=="hull":
        pen=0
    effective_dmg=(dmg-dmg*pen)*bonus
    hp=hp-effective_dmg
    if hp<=0:
        remaining_dmg=((-1*hp)/bonus)+(dmg*pen)
        remaining_hp=0
    else:
        remaining_hp=hp
        remaining_dmg=dmg*pen
    return(remaining_hp,remaining_dmg)



def do_nothing():
    x=1
    return()


        
if 1==1:
    main()
