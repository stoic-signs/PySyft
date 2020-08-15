# external classs imports
from typing import Optional, Union

from nacl.signing import SigningKey
from nacl.signing import VerifyKey

# external decorators
from typing_extensions import final

# syft imports
from ...io.location import SpecificLocation
from ...common.message import SyftMessage, SignedMessage
from ....decorators import syft_decorator
from .client import VirtualMachineClient
from ...io.location import Location
from ..common.node import Node
from ...common.uid import UID


@final
class VirtualMachine(Node):

    client_type = VirtualMachineClient
    vm: SpecificLocation  # redefine the type of self.vm to not be optional
    signing_key: Optional[SigningKey]
    verify_key: Optional[VerifyKey]
    child_type_client_type = None

    @syft_decorator(typechecking=True)
    def __init__(
        self,
        name: str,
        network: Optional[Location] = None,
        domain: Optional[Location] = None,
        device: Optional[Location] = None,
        vm: SpecificLocation = SpecificLocation(),
        signing_key: Optional[SigningKey] = None,
        verify_key: Optional[VerifyKey] = None,
    ):
        super().__init__(
            name=name,
            network=network,
            domain=domain,
            device=device,
            vm=vm,
            signing_key=signing_key,
            verify_key=verify_key,
        )

        # All node subclasses have to call this at the end of their __init__
        self._register_services()
        self.post_init()

    @property
    def icon(self) -> str:
        return "🍰"

    @property
    def id(self) -> UID:
        return self.vm.id

    def message_is_for_me(self, msg: Union[SyftMessage, SignedMessage]) -> bool:
        # this needs to be defensive by checking vm_id NOT vm.id or it breaks
        try:
            return msg.address.vm_id == self.id
        except Exception as e:
            error = f"Error checking if {msg.pprint} is for me on {self.pprint}. {e}"
            print(error)
            return False

    @syft_decorator(typechecking=True)
    def _register_frameworks(self) -> None:
        raise NotImplementedError
        # TODO: it doesn't at the moment but it needs to in the future,
        #  mostly because nodes should be able to choose waht framweorks they
        #  want to support (and more importantly what versions of those frameworks
        #  they want to support).
        # QUESTION: Does this exist?
        # from ....lib import supported_frameworks
        # for fw in supported_frameworks:
        #     for name, ast in fw.ast.attrs.items():
        #         if name in self.frameworks.attrs:
        #             raise KeyError(
        #                 "Framework already imported. Why are you importing it twice?"
        #             )
        #         self.frameworks.attrs[name] = ast