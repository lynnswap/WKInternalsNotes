# ``WKInternalsNotes/_WKProcessInfo/totalUserCPUTime``

ユーザ CPU 時間（秒）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSTimeInterval totalUserCPUTime;
```

## Default Value
`initWithTaskInfo:` で `info.totalUserCPUTime.seconds()` から設定される。

## Discussion
`TaskInfo` の user CPU time を秒に変換して保持する。

## References
- [`WKProcessPoolPrivate.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L58)
- [`WKProcessPool.mm#L743`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L743)
- [`WKProcessPool.mm#L769`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L769)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
