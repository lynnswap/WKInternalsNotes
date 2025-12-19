# ``WKInternalsNotes/WKProcessPool/_requestWebProcessTermination(_:)``

指定 PID の WebProcess に終了要求を送る。

## Objective-C Declaration
```objective-c
- (BOOL)_requestWebProcessTermination:(pid_t)pid WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`processes()` を走査し、pid 一致なら `requestTermination(RequestedByClient)` を呼ぶ。ループ内で YES を返すため、プロセスが存在すれば YES になる。

## References
- [`WKProcessPoolPrivate.h#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L155)
- [`WKProcessPool.mm#L438`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L438)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
