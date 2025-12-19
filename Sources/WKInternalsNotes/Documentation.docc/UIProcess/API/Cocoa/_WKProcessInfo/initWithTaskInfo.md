# ``WKInternalsNotes/_WKProcessInfo/initWithTaskInfo(_:)``

`TaskInfo` から `_WKProcessInfo` を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithTaskInfo:(const WebKit::AuxiliaryProcessProxy::TaskInfo&)info;
```

## Discussion
`info` から PID/状態/CPU 時間/physical footprint を読み取り、`processStateFromThrottleState` で状態を変換して各プロパティを設定する。

## References
- [`WKProcessPool.mm#L747`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L747)
- [`WKProcessPool.mm#L762`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L762)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
