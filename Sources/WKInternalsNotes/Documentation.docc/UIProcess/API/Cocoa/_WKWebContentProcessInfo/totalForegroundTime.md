# ``WKInternalsNotes/_WKWebContentProcessInfo/totalForegroundTime``

フォアグラウンド滞在時間（秒）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSTimeInterval totalForegroundTime;
```

## Discussion
`WebProcessProxy::totalForegroundTime().seconds()` を初期化時に保持する。

## References
- [`WKProcessPoolPrivate.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L69)
- [`WKProcessPool.mm#L820`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L820)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
