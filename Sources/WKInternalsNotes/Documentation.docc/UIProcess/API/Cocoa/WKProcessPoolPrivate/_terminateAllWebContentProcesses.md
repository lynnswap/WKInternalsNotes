# ``WKInternalsNotes/WKProcessPool/_terminateAllWebContentProcesses()``

全ての WebContent プロセスを終了する。

## Objective-C Declaration
```objective-c
- (void)_terminateAllWebContentProcesses;
```

## Discussion
`terminateAllWebContentProcesses(ProcessTerminationReason::RequestedByClient)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L136)
- [`WKProcessPool.mm#L675`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L675)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
