# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/shouldRunServiceWorkersOnMainThreadForTesting``

テスト用に Service Worker をメインスレッドで動かすかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldRunServiceWorkersOnMainThreadForTesting WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `shouldRunServiceWorkersOnMainThreadForTesting` の値を返す。

## Discussion
getter は `_configuration->shouldRunServiceWorkersOnMainThreadForTesting()` を返し、setter は `_configuration->setShouldRunServiceWorkersOnMainThreadForTesting` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L66](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L66)
- [_WKWebsiteDataStoreConfiguration.mm#L731](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L731)
- [_WKWebsiteDataStoreConfiguration.mm#L736](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L736)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
