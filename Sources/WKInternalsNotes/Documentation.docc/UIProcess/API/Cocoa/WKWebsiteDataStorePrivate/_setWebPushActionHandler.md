# ``WKInternalsNotes/WKWebsiteDataStore/_setWebPushActionHandler(_:)``

Web Push アクション処理ハンドラを設定する。

## Objective-C Declaration
```objective-c
+ (void)_setWebPushActionHandler:(WKWebsiteDataStore *(^)(_WKWebPushAction *))handler WK_API_AVAILABLE(ios(18.2));
```

## Discussion
iOS では一度だけアクションハンドラと通知センターの delegate を登録し、ハンドラを設定する。他プラットフォームでは no-op。

## References
- [`WKWebsiteDataStorePrivate.h#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L154)
- [`WKWebsiteDataStore.mm#L1512`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1512)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
