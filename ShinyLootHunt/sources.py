from dataclasses import dataclass
from typing import List, Dict
from enum import Enum, auto
from unrealsdk.unreal import UStruct
from unrealsdk import make_struct

class DropOdds(Enum):
    OnePercent = 0
    TwoPercent = auto()
    FivePercent = auto()

@dataclass
class Source:
    check: str
    drop_pools: List[str]
    drop_odds: DropOdds
    drop_location: UStruct = None

Loot_Sources: List[Source] = [
    Source("GD_Population_Marauder.Balance.Unique.PawnBalance_Mobley", ["GD_Itempools.Runnables.Pool_Veruc_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Psycho.Balance.Unique.PawnBalance_McNally", ["GD_Itempools.Runnables.Pool_HammerBuster_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_PrimalBeast.Balance.Unique.PawnBalance_PrimalBeast_Warmong", ["GD_Itempools.Runnables.Pool_KerBlaster_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Psycho.Balance.Unique.PawnBalance_MadDog", ["GD_Itempools.Runnables.Pool_MadHous_Shiny"], DropOdds.OnePercent),
    Source("GD_Aster_Pop_Orcs.Balance.PawnBalance_Orc_WarlordSlog", ["GD_Itempools.Runnables.Pool_Ogre_Shiny"], DropOdds.FivePercent),
    Source("GD_Population_PrimalBeast.Balance.Unique.PawnBalance_PrimalBeast_KingMong", ["GD_Itempools.Runnables.Pool_Badaboom_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Skag.Balance.Unique.PawnBalance_Skagzilla", ["GD_Itempools.Runnables.Pool_Mongol_Shiny"], DropOdds.OnePercent),
    Source("GD_Skagzilla_Digi.Population.PawnBalance_Skagzilla_Digi", ["GD_Itempools.Runnables.Pool_Mongol_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_SpiderAnt.Balance.Unique.PawnBalance_SpiderantBlackQueen", ["GD_Itempools.Runnables.Pool_Nukem_Shiny"], DropOdds.TwoPercent),
    Source("GD_SpiderantBlackQueen_Digi.Population.PawnBalance_SpiderantBlackQueen_Digi", ["GD_Itempools.Runnables.Pool_Nukem_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Psycho.Balance.Unique.PawnBalance_IncineratorVanya_Combat", ["GD_Itempools.Runnables.Pool_Pyrophobia_Shiny"], DropOdds.TwoPercent),
    Source("GD_UndeadFirePsycho_Giant.Balance.PawnBalance_UndeadFirePsycho_Giant", ["GD_Itempools.Runnables.Pool_Pyrophobia_Shiny"], DropOdds.FivePercent),
    Source("GD_Population_Rat.Balance.Unique.PawnBalance_Laney", ["GD_Itempools.Runnables.Pool_Gub_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Psycho.Balance.Unique.PawnBalance_RakkMan", ["GD_Itempools.Runnables.Pool_Gunerang_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_PrimalBeast.Balance.Unique.PawnBalance_PrimalBeast_KnuckleDragger", ["GD_Itempools.Runnables.Pool_Hornet_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Nomad.Balance.Unique.PawnBalance_MrMercy", ["GD_Itempools.Runnables.Pool_Infinity_Shiny"], DropOdds.OnePercent),
    Source("GD_MrMercy_Digi.Balance.PawnBalance_MrMercy_Digi", ["GD_Itempools.Runnables.Pool_Infinity_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Marauder.Balance.Unique.PawnBalance_MickZaford_Combat", ["GD_Itempools.Runnables.Pool_Maggie_Shiny"], DropOdds.OnePercent),
    Source("GD_FlyntSon.Population.PawnBalance_FlyntSon", ["GD_Itempools.Runnables.Pool_ThunderballFists_Shiny"], DropOdds.TwoPercent),
    Source("GD_FlyntSon.Population.PawnBalance_FlyntSon_Run", ["GD_Itempools.Runnables.Pool_ThunderballFists_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Nomad.Balance.Unique.PawnBalance_Flynt", ["GD_Itempools.Runnables.Pool_ThunderballFists_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Psycho.Balance.Unique.PawnBalance_SavageLee", ["GD_Itempools.Runnables.Pool_UnkemptHarold_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Skag.Balance.Unique.PawnBalance_Tumbaa", ["GD_Itempools.Runnables.Pool_Deliverance_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Goliath.Balance.Unique.PawnBalance_SmashHead", ["GD_Itempools.Runnables.Pool_SledgesShotgun_Shiny"], DropOdds.TwoPercent),
    Source("GD_Aster_Pop_Golems.Balance.PawnBalance_GolemGold", ["GD_Itempools.Runnables.Pool_Infinity_Shiny", "GD_Itempools.Runnables.Pool_Deliverance_Shiny", "GD_Itempools.Runnables.Pool_SledgesShotgun_Shiny"], DropOdds.FivePercent),
    Source("GD_Population_Thresher.Balance.Unique.PawnBalance_Slappy", ["GD_Itempools.Runnables.Pool_Striker_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_BugMorph.Balance.Unique.PawnBalance_SirReginald", ["GD_Itempools.Runnables.Pool_BabyMaker_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Psycho.Balance.Unique.PawnBalance_Assassin3", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Assassin1_Digi.Population.PawnBalance_Assassin1_Digi", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Assassin2_Digi.Population.PawnBalance_Assassin2_Digi", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Assassin3_Digi.Population.PawnBalance_Assassin3_Digi", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Assassin4_Digi.Population.PawnBalance_Assassin4_Digi", ["GD_Itempools.Runnables.Pool_Emperor_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_SpiderAnt.Balance.Unique.PawnBalance_SpiderantScorch", ["GD_Itempools.Runnables.Pool_Hellfire_Shiny"], DropOdds.OnePercent),
    Source("GD_SpiderantScorch_Digi.Population.PawnBalance_SpiderantScorch_Digi", ["GD_Itempools.Runnables.Pool_Hellfire_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Marauder.Balance.Unique.PawnBalance_TectorHodunk_Combat", ["GD_Itempools.Runnables.Pool_Slagga_Shiny"], DropOdds.OnePercent),
    Source("GD_Aster_Pop_Spiders.Unique.PawnBalance_AngelBoss", ["GD_Itempools.Runnables.Pool_Veruc_Shiny", "GD_Itempools.Runnables.Pool_Slagga_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Loader.Balance.Unique.PawnBalance_LoaderGiant", ["GD_Itempools.Runnables.Pool_Invader_Shiny"], DropOdds.OnePercent),
    Source("GD_LoaderUltimateBadass_Digi.Population.PawnBalance_LoaderUltimateBadass_Digi", ["GD_Itempools.Runnables.Pool_Invader_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Creeper.Balance.PawnBalance_CreeperBadass", ["GD_Itempools.Runnables.Pool_Longbow_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Engineer.Balance.Unique.PawnBalance_Gettle", ["GD_Itempools.Runnables.Pool_Lyuda_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Rakk.Balance.Unique.PawnBalance_SonMothrakk", ["GD_Itempools.Runnables.Pool_Skullmasher_Shiny"], DropOdds.FivePercent),
    Source("GD_Sage_SM_DahliaMurderData.Population.PawnBalance_Sage_DahliaMurder_Creature", ["GD_Itempools.Runnables.Pool_Skullmasher_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Rat.Balance.Unique.PawnBalance_Dan", ["GD_Itempools.Runnables.Pool_StormFront_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Rat.Balance.Unique.PawnBalance_Lee", ["GD_Itempools.Runnables.Pool_StormFront_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Rat.Balance.Unique.PawnBalance_Mick", ["GD_Itempools.Runnables.Pool_StormFront_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Rat.Balance.Unique.PawnBalance_Ralph", ["GD_Itempools.Runnables.Pool_StormFront_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Marauder.Balance.PawnBalance_Boom", ["GD_Itempools.Runnables.Pool_BonusPackage_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Marauder.Balance.PawnBalance_BoomBoom", ["GD_Itempools.Runnables.Pool_BonusPackage_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Loader.Balance.Unique.PawnBalance_Willhelm", ["GD_Itempools.Runnables.Pool_LogansGun_Shiny", "GD_Itempools.Runnables.Pool_RollingThunder_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_BugMorph.Balance.PawnBalance_BugMorphUltimateBadass", ["GD_Itempools.Runnables.Pool_Quasar_Shiny"], DropOdds.FivePercent),
    Source("GD_Population_Rat.Balance.Unique.PawnBalance_Mortar", ["GD_Itempools.Runnables.Pool_Pandemic_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_BugMorph.Balance.PawnBalance_BugMorphRaid", ["GD_Itempools.Runnables.Pool_Norfleet_Shiny", "GD_Itempools.Runnables.Pool_NastySurprise_Shiny"], DropOdds.FivePercent),
    Source("GD_Aster_Pop_Wizards.Balance.PawnBalance_FireMage_Badass", ["GD_Itempools.Runnables.Pool_FireStorm_Shiny"], DropOdds.OnePercent),
    Source("GD_Z1_InMemoriamData.Balance.PawnBalance_Boll", ["GD_Itempools.Runnables.Pool_Fastball_Shiny"], DropOdds.OnePercent),
    Source("GD_Aster_Pop_Wizards.Balance.PawnBalance_Sorcerer_Badass", ["GD_Itempools.Runnables.Pool_ChainLightning_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Engineer.Balance.Unique.PawnBalance_Foreman", ["GD_Itempools.Runnables.Pool_BlackHole_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Crystalisk.Balance.Unique.PawnBalance_Blue", ["GD_Itempools.Runnables.Pool_FabledTortoise_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Thresher.Balance.Unique.PawnBalance_ThresherRaid", ["GD_Itempools.Runnables.Pool_Pitchfork_Shiny", "GD_Itempools.Runnables.Pool_HideofTerramorphous_Shiny"], DropOdds.OnePercent),
    Source("GD_Spycho.Population.PawnBalance_Spycho", ["GD_Itempools.Runnables.Pool_Hellfire_Shiny", "GD_Itempools.Runnables.Pool_Neogenator_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_SpiderAnt.Balance.Unique.PawnBalance_MonsterMash1", ["GD_Itempools.Runnables.Pool_Neogenator_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Engineer.Balance.Unique.PawnBalance_DJHyperion", ["GD_Itempools.Runnables.Pool_TheBee_Shiny"], DropOdds.OnePercent),
    Source("GD_Aster_Pop_Treant.Balance.PawnBalance_Treant", ["GD_Itempools.Runnables.Pool_TheBee_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Stalker.Balance.Unique.PawnBalance_Henry", ["GD_Itempools.Runnables.Pool_TheCradle_Shiny"], DropOdds.OnePercent),
    Source("GD_Population_Stalker.Balance.Unique.PawnBalance_Stalker_Simon", ["GD_Itempools.Runnables.Pool_TheTransformer_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Stalker.Balance.PawnBalance_StalkerChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_SpiderAnt.Balance.PawnBalance_SpiderantChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Skag.Balance.PawnBalance_SkagChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Rakk.Balance.PawnBalance_RakkChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_Midget.Balance.PawnBalance_MidgetChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Population_BugMorph.Balance.PawnBalance_BugMorphChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Orchid_Pop_Stalker.Balance.PawnBalance_Orchid_StalkerChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Orchid_Pop_SpiderAnt.Balance.PawnBalance_SpiderantChubby_Orchid", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Orchid_Pop_Skag.Balance.PawnBalance_SkagChubby_Orchid", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.TwoPercent),
    Source("GD_Aster_Pop_Skeletons.Balance.PawnBalance_SkeletonChubby", ["GD_Itempools.Runnables.Pool_Bunny_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny", "GD_Itempools.Runnables.Pool_Infinity_Shiny"], DropOdds.TwoPercent),
    Source("GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_32", ["GD_Itempools.Runnables.Pool_ConferenceCall_Shiny", "GD_Itempools.Runnables.Pool_Flakker_Shiny", "GD_Itempools.Runnables.Pool_Volcano_Shiny", "GD_Itempools.Runnables.Pool_Leech_Shiny", "GD_Itempools.Runnables.Pool_Impaler_Shiny"], DropOdds.OnePercent),
    Source("Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ApplyBehavior_59.Behavior_SpawnItems_6", ["GD_Itempools.Runnables.Pool_ConferenceCall_Shiny", "GD_Itempools.Runnables.Pool_Flakker_Shiny", "GD_Itempools.Runnables.Pool_Volcano_Shiny", "GD_Itempools.Runnables.Pool_Leech_Shiny", "GD_Itempools.Runnables.Pool_Impaler_Shiny"], DropOdds.OnePercent, make_struct("Vector", X=1016, Y=509, Z=644)),
    Source("Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ApplyBehavior_16.Behavior_SpawnItems_6", ["GD_Itempools.Runnables.Pool_ConferenceCall_Shiny", "GD_Itempools.Runnables.Pool_Flakker_Shiny", "GD_Itempools.Runnables.Pool_Volcano_Shiny", "GD_Itempools.Runnables.Pool_Leech_Shiny", "GD_Itempools.Runnables.Pool_Impaler_Shiny"], DropOdds.OnePercent, make_struct("Vector", X=1016, Y=509, Z=644)),
    Source("Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ApplyBehavior_12.Behavior_SpawnItems_6", ["GD_Itempools.Runnables.Pool_ConferenceCall_Shiny", "GD_Itempools.Runnables.Pool_Flakker_Shiny", "GD_Itempools.Runnables.Pool_Volcano_Shiny", "GD_Itempools.Runnables.Pool_Leech_Shiny", "GD_Itempools.Runnables.Pool_Impaler_Shiny"], DropOdds.OnePercent, make_struct("Vector", X=1016, Y=509, Z=644)),
    Source("Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ApplyBehavior_31.Behavior_SpawnItems_6", ["GD_Itempools.Runnables.Pool_ConferenceCall_Shiny", "GD_Itempools.Runnables.Pool_Flakker_Shiny", "GD_Itempools.Runnables.Pool_Volcano_Shiny", "GD_Itempools.Runnables.Pool_Leech_Shiny", "GD_Itempools.Runnables.Pool_Impaler_Shiny"], DropOdds.OnePercent, make_struct("Vector", X=1016, Y=509, Z=644)),
    Source("GD_ThresherShared.Anims.Anim_Raid_Death1:BehaviorProviderDefinition_29.Behavior_SpawnItems_46", ["GD_Itempools.Runnables.Pool_Pitchfork_Shiny", "GD_Itempools.Runnables.Pool_HideofTerramorphous_Shiny"], DropOdds.OnePercent),
    Source("GD_Orchid_RaidEngineer.Death.BodyDeath_Orchid_RaidEngineer:BehaviorProviderDefinition_6.Behavior_SpawnItems_203", ["GD_Itempools.Runnables.Pool_Shredifier_Shiny", "GD_Itempools.Runnables.Pool_Norfleet_Shiny", "GD_Itempools.Runnables.Pool_Pyrophobia_Shiny", "GD_Itempools.Runnables.Pool_Hornet_Shiny", "GD_Itempools.Runnables.Pool_SledgesShotgun_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.OnePercent),
    Source("GD_Orchid_RaidEngineer.Death.BodyDeath_Orchid_RaidEngineer:BehaviorProviderDefinition_6.Behavior_SpawnItems_204", ["GD_Itempools.Runnables.Pool_Shredifier_Shiny", "GD_Itempools.Runnables.Pool_Norfleet_Shiny", "GD_Itempools.Runnables.Pool_Pyrophobia_Shiny", "GD_Itempools.Runnables.Pool_Hornet_Shiny", "GD_Itempools.Runnables.Pool_SledgesShotgun_Shiny", "GD_Itempools.Runnables.Pool_WTF_Shiny"], DropOdds.OnePercent),
    Source("GD_HyperionBunkerBoss.Character.AIDef_BunkerBoss:AIBehaviorProviderDefinition_1.Behavior_SpawnItems_4", ["GD_Itempools.Runnables.Pool_Bitch_Shiny", "GD_Itempools.Runnables.Pool_TheSham_Shiny"], DropOdds.OnePercent),
    Source("Transient.Behavior_SpawnItems_Orchid_MasterGeeDeath", ["GD_Itempools.Runnables.Pool_Gunerang_Shiny", "GD_Itempools.Runnables.Pool_Striker_Shiny", "GD_Itempools.Runnables.Pool_Bitch_Shiny", "GD_Itempools.Runnables.Pool_Pitchfork_Shiny", "GD_Itempools.Runnables.Pool_StormFront_Shiny", "GD_Itempools.Runnables.Pool_TheBee_Shiny"], DropOdds.OnePercent),
    Source("GD_Anemone_Balance_Treasure.InteractiveObjects.InteractiveObj_Brothers_Pile:BehaviorProviderDefinition_13.Behavior_DropItems_39", ["GD_Itempools.Runnables.Pool_Thumpson_Shiny"], DropOdds.TwoPercent, make_struct("Vector", X=7002.21435546875, Y=37100.59375, Z=-55.1817474365))
]