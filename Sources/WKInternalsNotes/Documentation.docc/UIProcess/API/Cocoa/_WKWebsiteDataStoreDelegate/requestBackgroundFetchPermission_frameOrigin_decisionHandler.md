# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/requestBackgroundFetchPermission(_:frameOrigin:decisionHandler:)``

Background Fetch の許可可否を問い合わせる。

## Objective-C Declaration
```objective-c
- (void)requestBackgroundFetchPermission:(NSURL *)mainFrameURL frameOrigin:(NSURL *)frameURL  decisionHandler:(void (^)(bool isGranted))decisionHandler;
```

## Discussion
delegate が未実装の場合は `false` を返す。実装済みの場合は `CompletionHandlerCallChecker` を使って一度だけ完了させ、`topOrigin`/`frameOrigin` を URL に変換して delegate に渡す。

## References
- [`_WKWebsiteDataStoreDelegate.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L70)
- [`WKWebsiteDataStore.mm#L285`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L285)
- [`WKWebsiteDataStore.mm#L303`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L303)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
