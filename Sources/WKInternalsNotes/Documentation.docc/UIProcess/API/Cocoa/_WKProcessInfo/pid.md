# ``WKInternalsNotes/_WKProcessInfo/pid``

プロセスの PID を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) pid_t pid;
```

## Default Value
`initWithTaskInfo:` で `info.pid` から設定される。

## Discussion
`TaskInfo` から `_pid` を設定し、synthesize された getter が値を返す。

## References
- [`WKProcessPoolPrivate.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L56)
- [`WKProcessPool.mm#L741`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L741)
- [`WKProcessPool.mm#L767`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L767)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
