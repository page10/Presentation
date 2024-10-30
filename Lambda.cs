using System;
using UnityEngine;

namespace ToDelete
{
    public class Lambda
    {
        
        /// <summary>
        /// 以前的写法
        /// 需要根据calculator枚举来写switch，一旦多一种方法，就需要改这个函数
        /// </summary>
        public void DealDamage(Character attacker, Character defender, DamageCalculator calculator, int[] args)
        {
            int damage = calculator switch
            {
                //减法算法：火纹系列
                DamageCalculator.MinusMethod => attacker.Attack - defender.Defend,
                //除法算法：暴雪游戏系列
                DamageCalculator.TimesMethod => Mathf.RoundToInt(attacker.Attack *
                                                                 (defender.Defend * 1.000f /
                                                                  ((int)args[0] + defender.Defend))),
                //真实伤害：比如关卡等可能需要
                DamageCalculator.TrueDamage => (int)args[0],
                _ => 0
            };
            //说明问题，所以就不做buff处理了
            defender.Hp -= damage;
        }

        /// <summary>
        /// 现在的写法，Calculator是一个函数
        /// </summary>
        /// <param name="attacker"></param>
        /// <param name="defender"></param>
        /// <param name="damageCalculator"></param>
        /// <param name="args"></param>
        public void DealDamage(Character attacker, Character defender,
            Func<Character, Character, int[], int> damageCalculator, int[] args) =>
            defender.Hp -= damageCalculator?.Invoke(attacker, defender, args) ?? 0;

        /// <summary>
        /// 调用
        /// </summary>
        /// <param name="attacker"></param>
        /// <param name="defender"></param>
        public void DoAttack(Character attacker, Character defender)
        {
            //老的
            DealDamage(attacker, defender, DamageCalculator.MinusMethod, Array.Empty<int>());
            //现在的，做到了老的支持不了的
            DealDamage(attacker, defender,
                (a, d, param) => Mathf.RoundToInt(a.Attack * 3.000f / d.Defend), 
                Array.Empty<int>());
        }
        
        public class Character
        {
            public int Hp;
            public int Attack;
            public int Defend;
        }

        public enum DamageCalculator
        {
            MinusMethod,
            TimesMethod,
            TrueDamage
        }
    }
}