from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    
    class Meta:
        model = Resume
        fields = (
            'id', 'user_id', 'full_name', 'about', 'age', 'email', 'phone', 
            'skills', 'languages', 'education1', 'education2', 'education3', 
            'project1', 'project2', 'experience1', 'experience2', 
            'achievements', 'created_at', 'updated_at'
        )
        read_only_fields = ('user', 'created_at', 'updated_at') 


    def to_representation(self, instance):
        """Converts the Django model instance to a JSON-compatible dictionary.
        Transforms comma-separated strings into lists."""
        
        representation = super().to_representation(instance)
        
        list_fields = ['skills', 'languages', 'achievements']
        
        for field_name in list_fields:
            value = representation.get(field_name)
            if value:
                representation[field_name] = [s.strip() for s in value.split(',') if s.strip()]
            else:
                representation[field_name] = [] 
                
        return representation
    
    def to_internal_value(self, data):
        """Converts data from React (JSON/list) back into the format Django expects (string)."""
        
        mutable_data = data.copy()
        
        list_fields = ['skills', 'languages', 'achievements']
        
        for field_name in list_fields:
            value = mutable_data.get(field_name)
            if isinstance(value, list):
                mutable_data[field_name] = ', '.join([str(s).strip() for s in value if str(s).strip()])
                
        return super().to_internal_value(mutable_data)