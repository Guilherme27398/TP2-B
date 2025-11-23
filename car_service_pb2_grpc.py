
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import car_service_pb2 as car__service__pb2


class CarServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCarsByMake = channel.unary_unary(
                '/car_service.CarService/GetCarsByMake',
                request_serializer=car__service__pb2.MakeRequest.SerializeToString,
                response_deserializer=car__service__pb2.CarList.FromString,
                )
        self.GetCarsByState = channel.unary_unary(
                '/car_service.CarService/GetCarsByState',
                request_serializer=car__service__pb2.StateRequest.SerializeToString,
                response_deserializer=car__service__pb2.CarList.FromString,
                )
        self.GetAveragePriceByMake = channel.unary_unary(
                '/car_service.CarService/GetAveragePriceByMake',
                request_serializer=car__service__pb2.MakeRequest.SerializeToString,
                response_deserializer=car__service__pb2.AveragePrice.FromString,
                )
        self.XPathQuery = channel.unary_unary(
                '/car_service.CarService/XPathQuery',
                request_serializer=car__service__pb2.XPathRequest.SerializeToString,
                response_deserializer=car__service__pb2.CarList.FromString,
                )
        self.GetAllMakes = channel.unary_unary(
                '/car_service.CarService/GetAllMakes',
                request_serializer=car__service__pb2.Empty.SerializeToString,
                response_deserializer=car__service__pb2.MakeList.FromString,
                )
        self.GetAllStates = channel.unary_unary(
                '/car_service.CarService/GetAllStates',
                request_serializer=car__service__pb2.Empty.SerializeToString,
                response_deserializer=car__service__pb2.StateList.FromString,
                )
        self.StreamCarsByMake = channel.unary_stream(
                '/car_service.CarService/StreamCarsByMake',
                request_serializer=car__service__pb2.MakeRequest.SerializeToString,
                response_deserializer=car__service__pb2.Car.FromString,
                )
        self.StreamCarsByState = channel.unary_stream(
                '/car_service.CarService/StreamCarsByState',
                request_serializer=car__service__pb2.StateRequest.SerializeToString,
                response_deserializer=car__service__pb2.Car.FromString,
                )


class CarServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCarsByMake(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCarsByState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAveragePriceByMake(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def XPathQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllMakes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllStates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamCarsByMake(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamCarsByState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCarsByMake': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCarsByMake,
                    request_deserializer=car__service__pb2.MakeRequest.FromString,
                    response_serializer=car__service__pb2.CarList.SerializeToString,
            ),
            'GetCarsByState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCarsByState,
                    request_deserializer=car__service__pb2.StateRequest.FromString,
                    response_serializer=car__service__pb2.CarList.SerializeToString,
            ),
            'GetAveragePriceByMake': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAveragePriceByMake,
                    request_deserializer=car__service__pb2.MakeRequest.FromString,
                    response_serializer=car__service__pb2.AveragePrice.SerializeToString,
            ),
            'XPathQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.XPathQuery,
                    request_deserializer=car__service__pb2.XPathRequest.FromString,
                    response_serializer=car__service__pb2.CarList.SerializeToString,
            ),
            'GetAllMakes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllMakes,
                    request_deserializer=car__service__pb2.Empty.FromString,
                    response_serializer=car__service__pb2.MakeList.SerializeToString,
            ),
            'GetAllStates': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllStates,
                    request_deserializer=car__service__pb2.Empty.FromString,
                    response_serializer=car__service__pb2.StateList.SerializeToString,
            ),
            'StreamCarsByMake': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamCarsByMake,
                    request_deserializer=car__service__pb2.MakeRequest.FromString,
                    response_serializer=car__service__pb2.Car.SerializeToString,
            ),
            'StreamCarsByState': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamCarsByState,
                    request_deserializer=car__service__pb2.StateRequest.FromString,
                    response_serializer=car__service__pb2.Car.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'car_service.CarService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CarService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCarsByMake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/GetCarsByMake',
            car__service__pb2.MakeRequest.SerializeToString,
            car__service__pb2.CarList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCarsByState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/GetCarsByState',
            car__service__pb2.StateRequest.SerializeToString,
            car__service__pb2.CarList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAveragePriceByMake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/GetAveragePriceByMake',
            car__service__pb2.MakeRequest.SerializeToString,
            car__service__pb2.AveragePrice.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def XPathQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/XPathQuery',
            car__service__pb2.XPathRequest.SerializeToString,
            car__service__pb2.CarList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllMakes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/GetAllMakes',
            car__service__pb2.Empty.SerializeToString,
            car__service__pb2.MakeList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllStates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/GetAllStates',
            car__service__pb2.Empty.SerializeToString,
            car__service__pb2.StateList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamCarsByMake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/car_service.CarService/StreamCarsByMake',
            car__service__pb2.MakeRequest.SerializeToString,
            car__service__pb2.Car.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamCarsByState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/car_service.CarService/StreamCarsByState',
            car__service__pb2.StateRequest.SerializeToString,
            car__service__pb2.Car.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
