#==============================================================================
# I would look for the dependencies properly, but there are many files with
# spaces in them. Because of this I have made it so that it rebuilds
# everytime.

#==============================================================================
.PHONY: .FORCE

#==============================================================================
Recipes.html: .FORCE
	generate_recipes.py > $@

#==============================================================================
.FORCE:
