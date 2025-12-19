# ``WKInternalsNotes/_WKWebContentProcessInfo/totalBackgroundTime``

バックグラウンド滞在時間（秒）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSTimeInterval totalBackgroundTime;
```

## Discussion
`WebProcessProxy::totalBackgroundTime().seconds()` を初期化時に保持する。

## References
- [`WKProcessPoolPrivate.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L70)
- [`WKProcessPool.mm#L821`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L821)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
