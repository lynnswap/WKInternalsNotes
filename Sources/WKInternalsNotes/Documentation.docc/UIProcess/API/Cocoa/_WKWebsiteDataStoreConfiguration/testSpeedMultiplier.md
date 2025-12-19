# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/testSpeedMultiplier``

テスト用の速度倍率を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger testSpeedMultiplier WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `testSpeedMultiplier` の値を返す。

## Discussion
getter は `_configuration->testSpeedMultiplier()` を返し、setter は `_configuration->setTestSpeedMultiplier` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L89](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L89)
- [_WKWebsiteDataStoreConfiguration.mm#L636](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L636)
- [_WKWebsiteDataStoreConfiguration.mm#L641](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L641)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
