# ``WKInternalsNotes/WKContentWorld/_worldWithConfiguration(_:)``

設定値から ContentWorldOption を組み立て、共有 world を返す。

## Objective-C Declaration
```objective-c
+ (WKContentWorld *)_worldWithConfiguration:(_WKContentWorldConfiguration *)configuration NS_SWIFT_NAME(worldWithConfiguration(configuration:)) WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`_WKContentWorldConfiguration` の各フラグを `OptionSet<WebKit::ContentWorldOption>` に反映し、`API::ContentWorld::sharedWorldWithName(configuration.name, optionSet)` で共有 world を取得する。その後 `checkContentWorldOptions` を呼び、既存 world のオプションと一致しない場合は `NSInternalInconsistencyException` を投げる。最後にラッパーを `autorelease` して返す。

## References
- [`WKContentWorldPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorldPrivate.h#L33)
- [`WKContentWorld.mm#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L32)
- [`WKContentWorld.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
