# ``WKInternalsNotes/_WKProcessInfo/state``

プロセスの実行状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKProcessState state;
```

## Default Value
`initWithTaskInfo:` で `info.state` を `processStateFromThrottleState` で変換して設定される。

## Discussion
`WebKit::ProcessThrottleState` を `_WKProcessState` に変換し、synthesize された getter で返す。

## References
- [`WKProcessPoolPrivate.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L57)
- [`WKProcessPool.mm#L742`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L742)
- [`WKProcessPool.mm#L747`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L747)
- [`WKProcessPool.mm#L768`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L768)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
