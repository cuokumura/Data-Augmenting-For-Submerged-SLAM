/**
* This file is part of our ROB530. This is strictly no warrantee!
*/


#ifndef DEPTHTYPES_H
#define DEPTHTYPES_H

#include <vector>
#include <utility>
#include <opencv2/core/core.hpp>
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <Eigen/Dense>
#include <sophus/se3.hpp>
#include <mutex>

#include "SerializationUtils.h"

#include <boost/serialization/serialization.hpp>
#include <boost/serialization/vector.hpp>

namespace ORB_SLAM3
{

namespace DEPTH
{

class Point
{
public:
    Point(const float &depth, const double &timestamp): d(depth),t(timestamp){};
public:
    double d; //<- Depth of measurement
    double t;
};

class PreparedPoint
{
    public:
        PreparedPoint(vector<Point> samples);
        ~PreparedPoint();
};

}

}
#endif // DEPTHTYPES_H
