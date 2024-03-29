// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from eufs_msgs:msg/ConeArrayWithCovariancePlus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "eufs_msgs/msg/detail/cone_array_with_covariance_plus__rosidl_typesupport_introspection_c.h"
#include "eufs_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "eufs_msgs/msg/detail/cone_array_with_covariance_plus__functions.h"
#include "eufs_msgs/msg/detail/cone_array_with_covariance_plus__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `cones`
#include "eufs_msgs/msg/cone_with_covariance_plus.h"
// Member `cones`
#include "eufs_msgs/msg/detail/cone_with_covariance_plus__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  eufs_msgs__msg__ConeArrayWithCovariancePlus__init(message_memory);
}

void eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_fini_function(void * message_memory)
{
  eufs_msgs__msg__ConeArrayWithCovariancePlus__fini(message_memory);
}

size_t eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__size_function__ConeArrayWithCovariancePlus__cones(
  const void * untyped_member)
{
  const eufs_msgs__msg__ConeWithCovariancePlus__Sequence * member =
    (const eufs_msgs__msg__ConeWithCovariancePlus__Sequence *)(untyped_member);
  return member->size;
}

const void * eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__get_const_function__ConeArrayWithCovariancePlus__cones(
  const void * untyped_member, size_t index)
{
  const eufs_msgs__msg__ConeWithCovariancePlus__Sequence * member =
    (const eufs_msgs__msg__ConeWithCovariancePlus__Sequence *)(untyped_member);
  return &member->data[index];
}

void * eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__get_function__ConeArrayWithCovariancePlus__cones(
  void * untyped_member, size_t index)
{
  eufs_msgs__msg__ConeWithCovariancePlus__Sequence * member =
    (eufs_msgs__msg__ConeWithCovariancePlus__Sequence *)(untyped_member);
  return &member->data[index];
}

void eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__fetch_function__ConeArrayWithCovariancePlus__cones(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const eufs_msgs__msg__ConeWithCovariancePlus * item =
    ((const eufs_msgs__msg__ConeWithCovariancePlus *)
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__get_const_function__ConeArrayWithCovariancePlus__cones(untyped_member, index));
  eufs_msgs__msg__ConeWithCovariancePlus * value =
    (eufs_msgs__msg__ConeWithCovariancePlus *)(untyped_value);
  *value = *item;
}

void eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__assign_function__ConeArrayWithCovariancePlus__cones(
  void * untyped_member, size_t index, const void * untyped_value)
{
  eufs_msgs__msg__ConeWithCovariancePlus * item =
    ((eufs_msgs__msg__ConeWithCovariancePlus *)
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__get_function__ConeArrayWithCovariancePlus__cones(untyped_member, index));
  const eufs_msgs__msg__ConeWithCovariancePlus * value =
    (const eufs_msgs__msg__ConeWithCovariancePlus *)(untyped_value);
  *item = *value;
}

bool eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__resize_function__ConeArrayWithCovariancePlus__cones(
  void * untyped_member, size_t size)
{
  eufs_msgs__msg__ConeWithCovariancePlus__Sequence * member =
    (eufs_msgs__msg__ConeWithCovariancePlus__Sequence *)(untyped_member);
  eufs_msgs__msg__ConeWithCovariancePlus__Sequence__fini(member);
  return eufs_msgs__msg__ConeWithCovariancePlus__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_member_array[2] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeArrayWithCovariancePlus, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "cones",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeArrayWithCovariancePlus, cones),  // bytes offset in struct
    NULL,  // default value
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__size_function__ConeArrayWithCovariancePlus__cones,  // size() function pointer
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__get_const_function__ConeArrayWithCovariancePlus__cones,  // get_const(index) function pointer
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__get_function__ConeArrayWithCovariancePlus__cones,  // get(index) function pointer
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__fetch_function__ConeArrayWithCovariancePlus__cones,  // fetch(index, &value) function pointer
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__assign_function__ConeArrayWithCovariancePlus__cones,  // assign(index, value) function pointer
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__resize_function__ConeArrayWithCovariancePlus__cones  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_members = {
  "eufs_msgs__msg",  // message namespace
  "ConeArrayWithCovariancePlus",  // message name
  2,  // number of fields
  sizeof(eufs_msgs__msg__ConeArrayWithCovariancePlus),
  eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_member_array,  // message members
  eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_init_function,  // function to initialize message memory (memory has to be allocated)
  eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_type_support_handle = {
  0,
  &eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_eufs_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, eufs_msgs, msg, ConeArrayWithCovariancePlus)() {
  eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, eufs_msgs, msg, ConeWithCovariancePlus)();
  if (!eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_type_support_handle.typesupport_identifier) {
    eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &eufs_msgs__msg__ConeArrayWithCovariancePlus__rosidl_typesupport_introspection_c__ConeArrayWithCovariancePlus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
