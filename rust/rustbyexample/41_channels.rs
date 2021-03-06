use std::comm;
use std::thread::Thread;

static NTHREADS: uint = 3;

fn main() {
    // Channels have two endpoints: the 'Sender<T>' and the 'Receiver<T>', where 'T' is the type of
    // the message to be transfered.
    // (type annotation is superfluous)
    let (tx, rx): (Sender<uint>, Receiver<uint>) = comm::channel();

    for id in range(0, NTHREADS) {
        // The sender endpoint can be copied
        let thread_tx = tx.clone();

        // Each thread will send its id via the channel
        Thread::spawn(move || {
            // The thread takes ownership over 'thread_tx'
            // Each thread queues a message in the channel
            thread_tx.send(id);

            // Sending is a non-blocking operation, the thread will continue immediately after
            // sending its message
            println!("thread {} finished", id);
        }).detach();
    }

    // Here, all the messages are collected
    let mut ids = Vec::with_capacity(NTHREADS);
    for _ in range(0, NTHREADS) {
        // The 'recv' method picks a message from the channel
        // 'recv' will block the current thread if there are no messages available
        ids.push(rx.recv());
    }

    // Show the order in which the messages were sent
    println!("{}", ids);
}
