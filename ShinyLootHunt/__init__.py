from typing import Any, List
import unrealsdk
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WeakPointer, UStruct, IGNORE_STRUCT
from mods_base import get_pc, build_mod, hook, ENGINE, SliderOption, BoolOption, HiddenOption, keybind, ButtonOption
from ui_utils import TrainingBox, show_hud_message, OptionBox, OptionBoxButton
import os
import sys
from pathlib import Path
from legacy_compat import legacy_compat
from .sources import DropOdds, Source, Loot_Sources
from random import randint

if True:
    try:
        assert __import__("command_extensions").__version_info__ >= (3,), "[Shiny Loot Hunt] Please Install Command Extensions"
    except (AssertionError, ImportError) as ex:
        import webbrowser
        webbrowser.open("https://bl-sdk.github.io/willow2-mod-db/mods/command-extensions/")
        raise ex

    with legacy_compat():
        try:
            import Mods.SanitySaver
        except:
            import webbrowser
            webbrowser.open("https://bl-sdk.github.io/willow2-mod-db/mods/sanitysaver/")
            print("\n[Shiny Loot Hunt] Please Install Sanity Saver\n")


ShinyVeruc: HiddenOption = HiddenOption("Shiny Veruc", False)
ShinyHammerBuster: HiddenOption = HiddenOption("Shiny Hammer Buster", False)
ShinyKerBlaster: HiddenOption = HiddenOption("Shiny KerBlaster", False)
ShinyThumpson: HiddenOption = HiddenOption("Shiny Thumpson", False)
ShinyMadhous: HiddenOption = HiddenOption("Shiny Madhous", False)
ShinyOgre: HiddenOption = HiddenOption("Shiny Ogre", False)
ShinyShredifier: HiddenOption = HiddenOption("Shiny Shredifier", False)

ShinyBadaboom: HiddenOption = HiddenOption("Shiny Badaboom", False)
ShinyBunny: HiddenOption = HiddenOption("Shiny Bunny", False)
ShinyMongol: HiddenOption = HiddenOption("Shiny Mongol", False)
ShinyNorfleet: HiddenOption = HiddenOption("Shiny Norfleet", False)
ShinyNukem: HiddenOption = HiddenOption("Shiny Nukem", False)
ShinyPyrophobia: HiddenOption = HiddenOption("Shiny Pyrophobia", False)

ShinyGub: HiddenOption = HiddenOption("Shiny Gub", False)
ShinyGunerang: HiddenOption = HiddenOption("Shiny Gunerang", False)
ShinyHornet: HiddenOption = HiddenOption("Shiny Hornet", False)
ShinyInfinity: HiddenOption = HiddenOption("Shiny Infinity", False)
ShinyLogansGun: HiddenOption = HiddenOption("Shiny Logans Gun", False)
ShinyMaggie: HiddenOption = HiddenOption("Shiny Maggie", False)
ShinyThunderballFists: HiddenOption = HiddenOption("Shiny Thunderball Fists", False)
ShinyUnkemptHarold: HiddenOption = HiddenOption("Shiny Unkempt Harold", False)

ShinyConferenceCall: HiddenOption = HiddenOption("Shiny Conference Call", False)
ShinyDeliverance: HiddenOption = HiddenOption("Shiny Deliverance", False)
ShinyFlakker: HiddenOption = HiddenOption("Shiny Flakker", False)
ShinySledgesShotgun: HiddenOption = HiddenOption("Shiny Sledges Shotgun", False)
ShinyStriker: HiddenOption = HiddenOption("Shiny Striker", False)

ShinyBabyMaker: HiddenOption = HiddenOption("Shiny Baby Maker", False)
ShinyBitch: HiddenOption = HiddenOption("Shiny Bitch", False)
ShinyEmperor: HiddenOption = HiddenOption("Shiny Emperor", False)
ShinyHellfire: HiddenOption = HiddenOption("Shiny Hellfire", False)
ShinySlagga: HiddenOption = HiddenOption("Shiny Slagga", False)

ShinyInvader: HiddenOption = HiddenOption("Shiny Invader", False)
ShinyLongbow: HiddenOption = HiddenOption("Shiny Longbow", False)
ShinyLyuda: HiddenOption = HiddenOption("Shiny Lyuda", False)
ShinyPitchfork: HiddenOption = HiddenOption("Shiny Pitchfork", False)
ShinySkullmasher: HiddenOption = HiddenOption("Shiny Skullmasher", False)
ShinyVolcano: HiddenOption = HiddenOption("Shiny Volcano", False)

ShinyStormFront: HiddenOption = HiddenOption("Shiny Storm Front", False)
ShinyRollingThunder: HiddenOption = HiddenOption("Shiny Rolling Thunder", False)
ShinyQuasar: HiddenOption = HiddenOption("Shiny Quasar", False)
ShinyPandemic: HiddenOption = HiddenOption("Shiny Pandemic", False)
ShinyNastySurprise: HiddenOption = HiddenOption("Shiny Nasty Surprise", False)
ShinyLeech: HiddenOption = HiddenOption("Shiny Leech", False)
ShinyFireStorm: HiddenOption = HiddenOption("Shiny Fire Storm", False)
ShinyFastball: HiddenOption = HiddenOption("Shiny Fastball", False)
ShinyChainLightning: HiddenOption = HiddenOption("Shiny Chain Lightning", False)
ShinyBonusPackage: HiddenOption = HiddenOption("Shiny Bonus Package", False)

ShinyBlackHole: HiddenOption = HiddenOption("Shiny Black Hole", False)
ShinyFabledTortoise: HiddenOption = HiddenOption("Shiny Fabled Tortoise", False)
ShinyHideofTerramorphous: HiddenOption = HiddenOption("Shiny Hide of Terramorphous", False)
ShinyImpaler: HiddenOption = HiddenOption("Shiny Impaler", False)
ShinyNeogenator: HiddenOption = HiddenOption("Shiny Neogenator", False)
ShinyTheBee: HiddenOption = HiddenOption("Shiny The Bee", False)
ShinyTheCradle: HiddenOption = HiddenOption("Shiny The Cradle", False)
ShinyTheSham: HiddenOption = HiddenOption("Shiny The Sham", False)
ShinyTheTransformer: HiddenOption = HiddenOption("Shiny The Transformer", False)
ShinyWhiskyTangoFoxtrot: HiddenOption = HiddenOption("Shiny Whisky Tango Foxtrot", False)

ars = [ ShinyHammerBuster, ShinyKerBlaster, ShinyMadhous, ShinyOgre, ShinyShredifier, ShinyThumpson, ShinyVeruc ]
launchers = [ ShinyBadaboom, ShinyBunny, ShinyMongol, ShinyNorfleet, ShinyNukem, ShinyPyrophobia ]
pistols = [ ShinyGub, ShinyGunerang, ShinyHornet, ShinyInfinity, ShinyLogansGun, ShinyMaggie, ShinyThunderballFists, ShinyUnkemptHarold ]
shotguns = [ ShinyConferenceCall, ShinyDeliverance, ShinyFlakker, ShinySledgesShotgun, ShinyStriker ]
smgs = [ ShinyBabyMaker, ShinyBitch, ShinyEmperor, ShinyHellfire, ShinySlagga ]
snipers = [ ShinyInvader, ShinyLongbow, ShinyLyuda, ShinyPitchfork, ShinySkullmasher, ShinyVolcano ]
grenades = [ ShinyBonusPackage, ShinyChainLightning, ShinyFastball, ShinyFireStorm, ShinyLeech, ShinyNastySurprise, ShinyPandemic, ShinyQuasar, ShinyRollingThunder, ShinyStormFront ]
shields = [ ShinyBlackHole, ShinyFabledTortoise, ShinyHideofTerramorphous, ShinyImpaler, ShinyNeogenator, ShinyTheBee, ShinyTheCradle, ShinyTheSham, ShinyTheTransformer, ShinyWhiskyTangoFoxtrot ]

ResetShinys: ButtonOption = ButtonOption("Reset Shiny Tracker", on_press= lambda _: ChoiceResetShinyList(_))

def ChoiceResetShinyList(_: ButtonOption) -> None:
    menu: OptionBox = OptionBox(
        title="Reset Shinys?",
        message="Are you really sure u wanna do this?\nThis will reset the shiny tracker but not delete any items you may have.",
        prevent_cancelling=True,
        buttons=[
            OptionBoxButton("No"),
            OptionBoxButton("Yes"),
        ],
    )

    menu.on_select = lambda self, button: {
        "No": DontResetShinyList,
        "Yes": ResetShinyList,
    }[button.name]()
    menu.show()
    return None


def ResetShinyList() -> None:
    global ars, launchers, pistols, shotguns, smgs, snipers, grenades, shields
    allitems = [ars, launchers, pistols, shotguns, smgs, snipers, grenades, shields]
    for category in allitems:
        for item in category:
            item.value = False
            item.save()
    return None

def DontResetShinyList() -> None:
    return None

def completionpercentage(count: int, max: int) -> int:
    return int(round((count / max) * 100, 0))

def getcolor(percentage: int) -> str:
    r = 0
    g = 0
    b = 0
    if percentage < 50:
        r = 255
        g = round(5.1 * percentage)
    else:
        g = 255
        r = round(510 - 5.1 * percentage)
    value = r * 0x10000 + g * 0x100 + b * 0x1
    return f"#{format(value, '06x')}"

@keybind("Show Shiny List")
def ShowShinyList() -> None:
    global ars, launchers, pistols, shotguns, smgs, snipers, grenades, shields
    total = 0

    arcount = 0
    for ar in ars:
        if ar.value == True:
            total += 1
            arcount += 1

    launchercount = 0
    for launcher in launchers:
        if launcher.value == True:
            total += 1
            launchercount += 1

    pistolcount = 0
    for pistol in pistols:
        if pistol.value == True:
            total += 1
            pistolcount += 1
    
    shotguncount = 0
    for shotgun in shotguns:
        if shotgun.value == True:
            total += 1
            shotguncount += 1

    smgcount = 0
    for smg in smgs:
        if smg.value == True:
            total += 1
            smgcount += 1

    snipercount = 0
    for sniper in snipers:
        if sniper.value == True:
            total += 1
            snipercount += 1
    
    grenadecount = 0
    for grenade in grenades:
        if grenade.value == True:
            total += 1
            grenadecount += 1

    shieldcount = 0
    for shield in shields:
        if shield.value == True:
            total += 1
            shieldcount += 1
    
    string = ""
    string += f"Total:  {total}/57  (<font color = \"{getcolor(completionpercentage(total, 57))}\" >{completionpercentage(total, 57)}%</font>)\n\n"
    string += f"Assault Rifles:  {arcount}/{len(ars)}  (<font color = \"{getcolor(completionpercentage(arcount, len(ars)))}\" >{completionpercentage(arcount, len(ars))}%</font>)\n"
    string += f"Rocket Launchers:  {launchercount}/{len(launchers)}  (<font color = \"{getcolor(completionpercentage(launchercount, len(launchers)))}\" >{completionpercentage(launchercount, len(launchers))}%</font>)\n"
    string += f"Pistols:  {pistolcount}/{len(pistols)}  (<font color = \"{getcolor(completionpercentage(pistolcount, len(pistols)))}\" >{completionpercentage(pistolcount, len(pistols))}%</font>)\n"
    string += f"Shotguns:  {shotguncount}/{len(shotguns)}  (<font color = \"{getcolor(completionpercentage(shotguncount, len(shotguns)))}\" >{completionpercentage(shotguncount, len(shotguns))}%</font>)\n"
    string += f"SMGs:  {smgcount}/{len(smgs)}  (<font color = \"{getcolor(completionpercentage(smgcount, len(smgs)))}\" >{completionpercentage(smgcount, len(smgs))}%</font>)\n"
    string += f"Sniper Rifles:  {snipercount}/{len(snipers)}  (<font color = \"{getcolor(completionpercentage(snipercount, len(snipers)))}\" >{completionpercentage(snipercount, len(snipers))}%</font>)\n"
    string += f"Grenades:  {grenadecount}/{len(grenades)}  (<font color = \"{getcolor(completionpercentage(grenadecount, len(grenades)))}\" >{completionpercentage(grenadecount, len(grenades))}%</font>)\n"
    string += f"Shields:  {shieldcount}/{len(shields)}  (<font color = \"{getcolor(completionpercentage(shieldcount, len(shields)))}\" >{completionpercentage(shieldcount, len(shields))}%</font>)\n"

    TrainingBox(title="Shiny Totals", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    
    DialogBoxCloseHook.enable()
    return None

@hook("WillowGame.WillowPickup:PickupAtRest", Type.PRE)
def PickupAtRestHook(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    if str(obj.Inventory.GetCategoryKey()) == "mod":
            if obj.Inventory.bGrenadeStored == False:
                return None
    elif str(obj.Inventory.GetCategoryKey()) in ("SMG", "Shotgun", "sniper", "ar", "Pistol", "rocket"):
        if obj.Inventory.StoredAmmo == 0:
            return None
    elif str(obj.Inventory.GetCategoryKey()) == "Shield":
        if obj.Inventory.ItemLocation == 5:
            return None
    if "_shiny" in str(obj.Inventory.DefinitionData.BalanceDefinition).lower():
        loc = obj.Location
        loc.Z += 100
        ENGINE.GetCurrentWorldInfo().MyEmitterPool.SpawnEmitter(unrealsdk.find_object("ParticleSystem", "FX_Aster_Magic.Particles.Part_MysteriousAmuletA"), loc, obj.Rotation)
        ENGINE.GetCurrentWorldInfo().MyEmitterPool.SpawnEmitter(unrealsdk.find_object("ParticleSystem", "FX_Aster_Magic.Particles.Part_MysteriousAmuletB"), loc, obj.Rotation)
        ENGINE.GetCurrentWorldInfo().MyEmitterPool.SpawnEmitter(unrealsdk.find_object("ParticleSystem", "FX_Aster_Magic.Particles.Part_MysteriousAmuletC"), loc, obj.Rotation)
    return None

@hook("WillowGame.WillowPickup:InitializeFromInventory", Type.POST)
def InitializeFromInventoryHook(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    if str(args.InInv.GetCategoryKey()) == "mod":
            if args.InInv.bGrenadeStored == False:
                return None
    elif str(args.InInv.GetCategoryKey()) in ("SMG", "Shotgun", "sniper", "ar", "Pistol", "rocket"):
        if args.InInv.StoredAmmo == 0:
            return None
    elif str(args.InInv.GetCategoryKey()) == "Shield":
        if args.InInv.ItemLocation == 5:
            return None
    if "_shiny" in str(args.InInv.DefinitionData.BalanceDefinition).lower():
        get_pc().PlayUIAkEvent(unrealsdk.find_object("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Token_Unlocked"))
    return None

def doPopup(item: str) -> None:
    get_pc().PlayUIAkEvent(unrealsdk.find_object("AkEvent", "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Token_Unlocked"))
    show_hud_message("Challenge Complete", f"Shiny {item}")
    return None

@hook("WillowGame.WillowPlayerController:HandlePickup", Type.PRE)
def HandlePickupHook(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    if str(args.Inv.GetCategoryKey()) in ("SMG", "Shotgun", "sniper", "ar", "Pistol", "rocket", "mod", "Shield"):
        if str(args.Inv.GetCategoryKey()) == "mod":
            if args.Inv.bGrenadeStored == False:
                return None
        elif str(args.Inv.GetCategoryKey()) == "Shield":
            if args.Inv.ItemLocation == 5:
                return None
        elif str(args.Inv.GetCategoryKey()) in ("SMG", "Shotgun", "sniper", "ar", "Pistol", "rocket"):
            if args.Inv.StoredAmmo == 0:
                return None
        balancedefinition = args.Inv.DefinitionData.BalanceDefinition
        if "_shiny" in str(balancedefinition).lower():
            #crimes
            if "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Dahl_5_Veruc_Shiny" in str(balancedefinition) and ShinyVeruc.value == False:
                ShinyVeruc.value = True
                ShinyVeruc.save()
                doPopup("Veruc")
            elif "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBuster_Shiny" in str(balancedefinition) and ShinyHammerBuster.value == False:
                ShinyHammerBuster.value = True
                ShinyHammerBuster.save()
                doPopup("Hammer Buster")
            elif "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Torgue_5_KerBlaster_Shiny" in str(balancedefinition) and ShinyKerBlaster.value == False:
                ShinyKerBlaster.value = True
                ShinyKerBlaster.save()
                doPopup("KerBlaster")
            elif "GD_Anemone_Weapons.AssaultRifle.Brothers.AR_Jakobs_5_Brothers_Shiny" in str(balancedefinition) and ShinyThumpson.value == False:
                ShinyThumpson.value = True
                ShinyThumpson.save()
                doPopup("M2828 Thumpson")
            elif "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Bandit_5_Madhouse_Shiny" in str(balancedefinition) and ShinyMadhous.value == False:
                ShinyMadhous.value = True
                ShinyMadhous.save()
                doPopup("Madhous!")
            elif "GD_Aster_Weapons.AssaultRifles.AR_Bandit_3_Ogre_Shiny" in str(balancedefinition) and ShinyOgre.value == False:
                ShinyOgre.value = True
                ShinyOgre.save()
                doPopup("Ogre")
            elif "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Vladof_5_Sherdifier_Shiny" in str(balancedefinition) and ShinyShredifier.value == False:
                ShinyShredifier.value = True
                ShinyShredifier.save()
                doPopup("Shredifier")
            elif "GD_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom_Shiny" in str(balancedefinition) and ShinyBadaboom.value == False:
                ShinyBadaboom.value = True
                ShinyBadaboom.save()
                doPopup("Badaboom")
            elif "GD_Weap_Launchers.A_Weapons_Legendary.RL_Tediore_5_Bunny_Shiny" in str(balancedefinition) and ShinyBunny.value == False:
                ShinyBunny.value = True
                ShinyBunny.save()
                doPopup("Bunny")
            elif "GD_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol_Shiny" in str(balancedefinition) and ShinyMongol.value == False:
                ShinyMongol.value = True
                ShinyMongol.save()
                doPopup("Mongol")
            elif "GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet_Shiny" in str(balancedefinition) and ShinyNorfleet.value == False:
                ShinyNorfleet.value = True
                ShinyNorfleet.save()
                doPopup("Norfleet")
            elif "GD_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem_Shiny" in str(balancedefinition) and ShinyNukem.value == False:
                ShinyNukem.value = True
                ShinyNukem.save()
                doPopup("Nukem")
            elif "GD_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Pyrophobia_Shiny" in str(balancedefinition) and ShinyPyrophobia.value == False:
                ShinyPyrophobia.value = True
                ShinyPyrophobia.save()
                doPopup("Pyrophobia")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Gub_Shiny" in str(balancedefinition) and ShinyGub.value == False:
                ShinyGub.value = True
                ShinyGub.save()
                doPopup("Gub")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Gunerang_Shiny" in str(balancedefinition) and ShinyGunerang.value == False:
                ShinyGunerang.value = True
                ShinyGunerang.save()
                doPopup("Gunerang")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Hornet_Shiny" in str(balancedefinition) and ShinyHornet.value == False:
                ShinyHornet.value = True
                ShinyHornet.save()
                doPopup("Hornet")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Vladof_5_Infinity_Shiny" in str(balancedefinition) and ShinyInfinity.value == False:
                ShinyInfinity.value = True
                ShinyInfinity.save()
                doPopup("Infinity")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun_Shiny" in str(balancedefinition) and ShinyLogansGun.value == False:
                ShinyLogansGun.value = True
                ShinyLogansGun.save()
                doPopup("Logan's Gun")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie_Shiny" in str(balancedefinition) and ShinyMaggie.value == False:
                ShinyMaggie.value = True
                ShinyMaggie.save()
                doPopup("Maggie")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Maliwan_5_ThunderballFists_Shiny" in str(balancedefinition) and ShinyThunderballFists.value == False:
                ShinyThunderballFists.value = True
                ShinyThunderballFists.save()
                doPopup("Thunderball Fists")
            elif "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla_Shiny" in str(balancedefinition) and ShinyUnkemptHarold.value == False:
                ShinyUnkemptHarold.value = True
                ShinyUnkemptHarold.save()
                doPopup("Unkempt Harold")
            elif "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall_Shiny" in str(balancedefinition) and ShinyConferenceCall.value == False:
                ShinyConferenceCall.value = True
                ShinyConferenceCall.save()
                doPopup("Conference Call")
            elif "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Tediore_5_Deliverance_Shiny" in str(balancedefinition) and ShinyDeliverance.value == False:
                ShinyDeliverance.value = True
                ShinyDeliverance.save()
                doPopup("Deliverance")
            elif "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker_Shiny" in str(balancedefinition) and ShinyFlakker.value == False:
                ShinyFlakker.value = True
                ShinyFlakker.save()
                doPopup("Flakker")
            elif "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun_Shiny" in str(balancedefinition) and ShinySledgesShotgun.value == False:
                ShinySledgesShotgun.value = True
                ShinySledgesShotgun.save()
                doPopup("Sledge's Shotgun")
            elif "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker_Shiny" in str(balancedefinition) and ShinyStriker.value == False:
                ShinyStriker.value = True
                ShinyStriker.save()
                doPopup("Striker")
            elif "GD_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_BabyMaker_Shiny" in str(balancedefinition) and ShinyBabyMaker.value == False:
                ShinyBabyMaker.value = True
                ShinyBabyMaker.save()
                doPopup("Baby Maker")
            elif "GD_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch_Shiny" in str(balancedefinition) and ShinyBitch.value == False:
                ShinyBitch.value = True
                ShinyBitch.save()
                doPopup("Bitch")
            elif "GD_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Emperor_Shiny" in str(balancedefinition) and ShinyEmperor.value == False:
                ShinyEmperor.value = True
                ShinyEmperor.save()
                doPopup("Emperor")
            elif "GD_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire_Shiny" in str(balancedefinition) and ShinyHellfire.value == False:
                ShinyHellfire.value = True
                ShinyHellfire.save()
                doPopup("Hellfire")
            elif "GD_Weap_SMG.A_Weapons_Legendary.SMG_Bandit_5_Slagga_Shiny" in str(balancedefinition) and ShinySlagga.value == False:
                ShinySlagga.value = True
                ShinySlagga.save()
                doPopup("Slagga")
            elif "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader_Shiny" in str(balancedefinition) and ShinyInvader.value == False:
                ShinyInvader.value = True
                ShinyInvader.save()
                doPopup("Invader")
            elif "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Longbow_Shiny" in str(balancedefinition) and ShinyLongbow.value == False:
                ShinyLongbow.value = True
                ShinyLongbow.save()
                doPopup("Longbow")
            elif "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Lyudmila_Shiny" in str(balancedefinition) and ShinyLyuda.value == False:
                ShinyLyuda.value = True
                ShinyLyuda.save()
                doPopup("Lyuda")
            elif "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork_Shiny" in str(balancedefinition) and ShinyPitchfork.value == False:
                ShinyPitchfork.value = True
                ShinyPitchfork.save()
                doPopup("Pitchfork")
            elif "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher_Shiny" in str(balancedefinition) and ShinySkullmasher.value == False:
                ShinySkullmasher.value = True
                ShinySkullmasher.save()
                doPopup("Skullmasher")
            elif "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Volcano_Shiny" in str(balancedefinition) and ShinyVolcano.value == False:
                ShinyVolcano.value = True
                ShinyVolcano.save()
                doPopup("Volcano")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_StormFront_Shiny" in str(balancedefinition) and ShinyStormFront.value == False:
                ShinyStormFront.value = True
                ShinyStormFront.save()
                doPopup("Storm Front")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_RollingThunder_Shiny" in str(balancedefinition) and ShinyRollingThunder.value == False:
                ShinyRollingThunder.value = True
                ShinyRollingThunder.save()
                doPopup("Rolling Thunder")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_Quasar_Shiny" in str(balancedefinition) and ShinyQuasar.value == False:
                ShinyQuasar.value = True
                ShinyQuasar.save()
                doPopup("Quasar")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_Pandemic_Shiny" in str(balancedefinition) and ShinyPandemic.value == False:
                ShinyPandemic.value = True
                ShinyPandemic.save()
                doPopup("Pandemic")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_NastySurprise_Shiny" in str(balancedefinition) and ShinyNastySurprise.value == False:
                ShinyNastySurprise.value = True
                ShinyNastySurprise.save()
                doPopup("Nasty Surprise")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_Leech_Shiny" in str(balancedefinition) and ShinyLeech.value == False:
                ShinyLeech.value = True
                ShinyLeech.save()
                doPopup("Leech")
            elif "GD_Aster_GrenadeMods.A_Item.GM_FireStorm_Shiny" in str(balancedefinition) and ShinyFireStorm.value == False:
                ShinyFireStorm.value = True
                ShinyFireStorm.save()
                doPopup("Fire Storm")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_Fastball_Shiny" in str(balancedefinition) and ShinyFastball.value == False:
                ShinyFastball.value = True
                ShinyFastball.save()
                doPopup("Fastball")
            elif "GD_Aster_GrenadeMods.A_Item.GM_ChainLightning_Shiny" in str(balancedefinition) and ShinyChainLightning.value == False:
                ShinyChainLightning.value = True
                ShinyChainLightning.save()
                doPopup("Chain Lightning")
            elif "GD_GrenadeMods.A_Item_Legendary.GM_BonusPackage_Shiny" in str(balancedefinition) and ShinyBonusPackage.value == False:
                ShinyBonusPackage.value = True
                ShinyBonusPackage.save()
                doPopup("Bonus Package")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Singularity_Shiny" in str(balancedefinition) and ShinyBlackHole.value == False:
                ShinyBlackHole.value = True
                ShinyBlackHole.save()
                doPopup("Black Hole")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_05_Legendary_Shiny" in str(balancedefinition) and ShinyFabledTortoise.value == False:
                ShinyFabledTortoise.value = True
                ShinyFabledTortoise.save()
                doPopup("Fabled Tortoise")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_ThresherRaid_Shiny" in str(balancedefinition) and ShinyHideofTerramorphous.value == False:
                ShinyHideofTerramorphous.value = True
                ShinyHideofTerramorphous.save()
                doPopup("Hide of Terramorphous")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_05_Legendary_Shiny" in str(balancedefinition) and ShinyImpaler.value == False:
                ShinyImpaler.value = True
                ShinyImpaler.save()
                doPopup("Impaler")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_05_Legendary_Shiny" in str(balancedefinition) and ShinyNeogenator.value == False:
                ShinyNeogenator.value = True
                ShinyNeogenator.save()
                doPopup("Neogenator")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_05_Legendary_Shiny" in str(balancedefinition) and ShinyTheBee.value == False:
                ShinyTheBee.value = True
                ShinyTheBee.save()
                doPopup("The Bee")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_05_Legendary_Shiny" in str(balancedefinition) and ShinyTheCradle.value == False:
                ShinyTheCradle.value = True
                ShinyTheCradle.save()
                doPopup("The Cradle")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryNormal_Shiny" in str(balancedefinition) and ShinyTheSham.value == False:
                ShinyTheSham.value = True
                ShinyTheSham.save()
                doPopup("The Sham")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryShock_Shiny" in str(balancedefinition) and ShinyTheTransformer.value == False:
                ShinyTheTransformer.value = True
                ShinyTheTransformer.save()
                doPopup("The Transformer")
            elif "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_05_Legendary_Shiny" in str(balancedefinition) and ShinyWhiskyTangoFoxtrot.value == False:
                ShinyWhiskyTangoFoxtrot.value = True
                ShinyWhiskyTangoFoxtrot.save()
                doPopup("Whisky Tango Foxtrot")
    return None

@hook("WillowGame.WillowGFxTrainingDialogBox:OnClose", Type.POST)
def DialogBoxCloseHook(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    global launchers, pistols, shotguns, smgs, snipers, grenades, shields, ars
    if "shiny totals" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in ars:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny Assault Rifles", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny assault rifles" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in launchers:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny Launchers", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny launchers" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in pistols:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny Pistols", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny pistols" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in shotguns:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny Shotguns", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny shotguns" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in smgs:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny SMGs", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny smgs" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in snipers:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny Snipers", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny snipers" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in grenades:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny Grenades", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny grenades" in str(obj.DlgCaptionMarkup).lower():
        string = ""
        for thing in shields:
            string += f"{thing.identifier} "
            if thing.value:
                string += "[<font color = \"#ff0000\" >x</font>]\n"
            else:
                string += "[ ]\n"
        TrainingBox(title="Shiny Shields", message=string, min_duration=0, pauses_game=True, menu_hint=0, priority=255).show()
    elif "shiny shields" in str(obj.DlgCaptionMarkup).lower():
        DialogBoxCloseHook.disable()
    return None

def dropLoot(pool: str, location: UStruct) -> None:
    obj = unrealsdk.construct_object("Behavior_SpawnLootAroundPoint", ENGINE.Outer)
    obj.ItemPools = [unrealsdk.find_object("ItemPoolDefinition", pool)]
    obj.SpawnVelocityRelativeTo = 0
    obj.bTorque = False
    obj.CircularScatterRadius = 10
    obj.CustomLocation = unrealsdk.make_struct("AttachmentLocationData", Location=location, AttachmentBase=None, AttachmentName="")
    obj.ApplyBehaviorToContext(get_pc(), IGNORE_STRUCT, None, None, None, IGNORE_STRUCT)
    return None
debug = False
def tryDrop(src: Source, loc: UStruct) -> None:
    global debug
    if debug:
        for pool in src.drop_pools:
            if src.drop_location != None:
                dropLoot(pool, src.drop_location)
            else:
                dropLoot(pool, loc)
        return None
    if src.drop_odds == DropOdds.OnePercent:
        for pool in src.drop_pools:
            if randint(1, 100) == 69:
                if src.drop_location != None:
                    dropLoot(pool, src.drop_location)
                else:
                    dropLoot(pool, loc)
    elif src.drop_odds == DropOdds.TwoPercent:
        for pool in src.drop_pools:
            if randint(1, 100) in (67, 69):
                if src.drop_location != None:
                    dropLoot(pool, src.drop_location)
                else:
                    dropLoot(pool, loc)
    elif src.drop_odds == DropOdds.FivePercent:
        for pool in src.drop_pools:
            if randint(1, 100) in (12, 24, 25, 67, 69): # i know i could just check a range but i want the funny numbers ok
                if src.drop_location != None:
                    dropLoot(pool, src.drop_location)
                else:
                    dropLoot(pool, loc)
    return None

@hook("WillowGame.WillowAIPawn:Died", Type.PRE)
def AIPawnDiedHook(obj: UObject, args: WrappedStruct, ret: Any, _4: BoundFunction) -> None:
    for src in Loot_Sources:
        if obj.BalanceDefinitionState.BalanceDefinition != None:
            if obj.BalanceDefinitionState.BalanceDefinition._path_name() == src.check:
                loc = obj.Location
                loc.Z += 75
                tryDrop(src, loc)
                break
    return None

@hook("WillowGame.Behavior_DropItems:ApplyBehaviorToContext", Type.PRE)
@hook("WillowGame.Behavior_SpawnItems:ApplyBehaviorToContext", Type.PRE)
def SpawnItemsHook(obj: UObject, args: WrappedStruct, ret: Any, _4: BoundFunction) -> None:
    for src in Loot_Sources:
        if obj._path_name() == src.check:
            tryDrop(src, args.SelfObject.Location)
            break
    return None

@hook("Engine.Pawn:PlayWeaponSwitch", Type.POST_UNCONDITIONAL)
def PlayWeaponSwitchHook(obj: UObject, args: WrappedStruct, ret: Any, _4: BoundFunction) -> None:
    global debug
    if obj.BalanceDefinitionState.BalanceDefinition != None:
        if obj.BalanceDefinitionState.BalanceDefinition._path_name() == "GD_Anemone_Pop_NP.Balance.PawnBalance_NP_Lt_Angvar" and "WillowAIPawn_" in str(obj) and obj.ExpLevel != 0 and obj.bIsDead == False:
                if args.OldWeapon == None:
                    if randint(1, 100) == 69 or debug:
                        item = []
                        items = unrealsdk.find_class("ItemPool").ClassDefaultObject.SpawnBalancedInventoryFromPool(unrealsdk.find_object("ItemPoolDefinition", "GD_Itempools.Runnables.Pool_Infinity_Shiny"), get_pc().PlayerReplicationInfo.ExpLevel + get_pc().OverpowerChoiceValue, 1, get_pc(), item, bInventoryMayDropOnDeath=True)
                        items[1][0].GiveTo(obj, True)
    return None

@hook("WillowGame.FrontendGFxMovie:Start", Type.POST)
def LoadTextModHook(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    if ENGINE.GetCurrentWorldInfo().GetStreamingPersistentMapName().lower() == "menumap":
        path_to_mod_folder = os.path.relpath(Path(__file__).parent.resolve(), os.path.join(Path(sys.executable).parent.resolve(), "..//..//Binaries"))
        exec_path = os.path.join(path_to_mod_folder, f"shiny.blcm")
        get_pc().ConsoleCommand(f"exec {exec_path}")
        print(f"Ran {exec_path}")
        LoadTextModHook.disable()
    return None

def Enable() -> None:
    if unrealsdk.find_class("WillowDownloadableContentManager").ClassDefaultObject.IsInStartMenu() == False and ENGINE.GetCurrentWorldInfo().GetStreamingPersistentMapName().lower() == "menumap":
        try:
            unrealsdk.find_object("ItemPoolDefinition", "GD_Itempools.Runnables.Pool_Veruc_Shiny")
        except:
            path_to_mod_folder = os.path.relpath(Path(__file__).parent.resolve(), os.path.join(Path(sys.executable).parent.resolve(), "..//..//Binaries"))
            exec_path = os.path.join(path_to_mod_folder, f"shiny.blcm")
            get_pc().ConsoleCommand(f"exec {exec_path}")
            print(f"Ran on mod start {exec_path}")
            LoadTextModHook.disable()
    return None

build_mod(hooks=[PickupAtRestHook, HandlePickupHook, LoadTextModHook, InitializeFromInventoryHook, AIPawnDiedHook, SpawnItemsHook, PlayWeaponSwitchHook], on_enable=Enable)
