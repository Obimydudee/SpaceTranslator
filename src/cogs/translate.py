import discord
from discord import app_commands
import random
from Utils.ariralList import alien2english, english2alien
from Utils.gleeb import cipher, decipher

async def setup(client):
    @client.tree.command(name="ari-translate", description="Translate english to ariral or wise versa!")
    async def download(interaction: discord.Interaction, input: str):
        if input == "":
            await interaction.response.send_message("Input cannot be empty")
            return
        
        if any(c in input for c in ['θ', 'Æ', 'æ', 'œ', 'Θ']):
            await interaction.response.send_message(f"Estimated Translation: {alien2english(input)}")
        else:
            await interaction.response.send_message(f"Translated: {english2alien(input)}")

    @client.tree.command(name="gleeb-translate", description="Translate english to gleeb or wise versa!")
    async def gleeb(interaction: discord.Interaction, input: str):
        if input == "":
            await interaction.response.send_message("Input cannot be empty")
            return
        
        if any(c in input for c in ['⏃', '⏚', '⎅', '⌰', '⟒', '⎎', '☌', '⊑', '⟟', '⟊', '☍', '⌰', '⋔', '⋏', '⍜', '⌿', '⍾', '⍀', '⌇', '⏁', '⎍', '⎐', '⍙', '⌖', '⊬', '⋉']):
            await interaction.response.send_message(f"Estimated Translation: {decipher(input)}")
        else:
            await interaction.response.send_message(f"Translated: {cipher(input)}")