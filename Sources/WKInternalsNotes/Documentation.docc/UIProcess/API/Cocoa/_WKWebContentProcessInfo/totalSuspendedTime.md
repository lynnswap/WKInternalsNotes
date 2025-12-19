# ``WKInternalsNotes/_WKWebContentProcessInfo/totalSuspendedTime``

サスペンド滞在時間（秒）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSTimeInterval totalSuspendedTime;
```

## Discussion
`WebProcessProxy::totalSuspendedTime().seconds()` を初期化時に保持する。

## References
- [`WKProcessPoolPrivate.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L71)
- [`WKProcessPool.mm#L822`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L822)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
