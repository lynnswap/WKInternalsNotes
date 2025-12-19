# ``WKInternalsNotes/_WKProcessInfo/totalSystemCPUTime``

システム CPU 時間（秒）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSTimeInterval totalSystemCPUTime;
```

## Default Value
`initWithTaskInfo:` で `info.totalSystemCPUTime.seconds()` から設定される。

## Discussion
`TaskInfo` の system CPU time を秒に変換して保持する。

## References
- [`WKProcessPoolPrivate.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L59)
- [`WKProcessPool.mm#L744`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L744)
- [`WKProcessPool.mm#L770`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L770)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
