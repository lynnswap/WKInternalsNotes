# ``WKInternalsNotes/WKProcessPool/_isJITDisabledInAllRemoteWorkerProcesses(_:)``

全リモートワーカープロセスで JIT が無効かを非同期で返す。

## Objective-C Declaration
```objective-c
- (void)_isJITDisabledInAllRemoteWorkerProcesses:(void(^)(BOOL))completionHandler;
```

## Discussion
`isJITDisabledInAllRemoteWorkerProcesses` を呼び、結果を completionHandler に渡す。

## References
- [`WKProcessPoolPrivate.h#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L145)
- [`WKProcessPool.mm#L523`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L523)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
