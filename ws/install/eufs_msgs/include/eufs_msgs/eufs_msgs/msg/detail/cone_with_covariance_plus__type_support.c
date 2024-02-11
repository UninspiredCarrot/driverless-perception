// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from eufs_msgs:msg/ConeWithCovariancePlus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "eufs_msgs/msg/detail/cone_with_covariance_plus__rosidl_typesupport_introspection_c.h"
#include "eufs_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "eufs_msgs/msg/detail/cone_with_covariance_plus__functions.h"
#include "eufs_msgs/msg/detail/cone_with_covariance_plus__struct.h"


// Include directives for member types
// Member `point`
#include "geometry_msgs/msg/point.h"
// Member `point`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  eufs_msgs__msg__ConeWithCovariancePlus__init(message_memory);
}

void eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_fini_function(void * message_memory)
{
  eufs_msgs__msg__ConeWithCovariancePlus__fini(message_memory);
}

size_t eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__size_function__ConeWithCovariancePlus__covariance(
  const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__get_const_function__ConeWithCovariancePlus__covariance(
  const void * untyped_member, size_t index)
{
  const double * member =
    (const double *)(untyped_member);
  return &member[index];
}

void * eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__get_function__ConeWithCovariancePlus__covariance(
  void * untyped_member, size_t index)
{
  double * member =
    (double *)(untyped_member);
  return &member[index];
}

void eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__fetch_function__ConeWithCovariancePlus__covariance(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__get_const_function__ConeWithCovariancePlus__covariance(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__assign_function__ConeWithCovariancePlus__covariance(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__get_function__ConeWithCovariancePlus__covariance(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_member_array[7] = {
  {
    "id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeWithCovariancePlus, id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "blue_prob",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeWithCovariancePlus, blue_prob),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yellow_prob",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeWithCovariancePlus, yellow_prob),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "orange_prob",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeWithCovariancePlus, orange_prob),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "big_orange_prob",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeWithCovariancePlus, big_orange_prob),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "point",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeWithCovariancePlus, point),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "covariance",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(eufs_msgs__msg__ConeWithCovariancePlus, covariance),  // bytes offset in struct
    NULL,  // default value
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__size_function__ConeWithCovariancePlus__covariance,  // size() function pointer
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__get_const_function__ConeWithCovariancePlus__covariance,  // get_const(index) function pointer
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__get_function__ConeWithCovariancePlus__covariance,  // get(index) function pointer
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__fetch_function__ConeWithCovariancePlus__covariance,  // fetch(index, &value) function pointer
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__assign_function__ConeWithCovariancePlus__covariance,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_members = {
  "eufs_msgs__msg",  // message namespace
  "ConeWithCovariancePlus",  // message name
  7,  // number of fields
  sizeof(eufs_msgs__msg__ConeWithCovariancePlus),
  eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_member_array,  // message members
  eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_init_function,  // function to initialize message memory (memory has to be allocated)
  eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_type_support_handle = {
  0,
  &eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_eufs_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, eufs_msgs, msg, ConeWithCovariancePlus)() {
  eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_member_array[5].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_type_support_handle.typesupport_identifier) {
    eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &eufs_msgs__msg__ConeWithCovariancePlus__rosidl_typesupport_introspection_c__ConeWithCovariancePlus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
