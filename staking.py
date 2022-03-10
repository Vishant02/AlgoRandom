from pyteal import *
#staking contract
def approval_program():
    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp],
        [Txn.on_completion() == OnComplete.NoOp, handle_noop],
    )

    handle_noop = Seq([
        Approve()
    ])

    on_creation = Seq([
        Approve()
    ])

    handle_optin = Seq([
        Approve()
    ])

    handle_closeout = Seq([
        Approve()
    ])

    handle_updateapp = Seq([
        Approve()
    ])

    handle_deleteapp = Seq([
        Approve()
    ])

    return compileTeal(program, Mode.Application, version = 5)


def clear_state_program():
    program = Return(Int(1))
    return compileTeal(program, Mode.Application, version=5)