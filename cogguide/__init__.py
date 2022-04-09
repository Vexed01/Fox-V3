from .cogguide import CogGuide


async def setup(bot):
    await bot.add_cog(CogGuide(bot))
