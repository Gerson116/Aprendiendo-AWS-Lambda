#!/bin/bash
# Crear usuarios en AWS IAM
aws iam create-user --user-name LuisJoseGuzmanSena
aws iam create-user --user-name AnaMariaLopezDiaz
aws iam create-user --user-name CarlosEduardoMartinezRuiz

# Asignar permisos que solo den acceso de lectura
aws iam attach-user-policy --user-name LuisJoseGuzmanSena --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess
aws iam attach-user-policy --user-name AnaMariaLopezDiaz --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess
aws iam attach-user-policy --user-name CarlosEduardoMartinezRuiz --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess

# Verificar si los usuarios tienen los permisos asignados
aws iam list-attached-user-policies --user-name LuisJoseGuzmanSena
aws iam list-attached-user-policies --user-name AnaMariaLopezDiaz
aws iam list-attached-user-policies --user-name CarlosEduardoMartinezRuiz