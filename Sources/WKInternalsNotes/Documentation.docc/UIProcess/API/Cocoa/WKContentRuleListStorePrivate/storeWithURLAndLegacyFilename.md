# ``WKInternalsNotes/WKContentRuleListStore/storeWithURLAndLegacyFilename(_:)``

URL で指定したパスのストアをレガシーファイル名前提で返す。

## Objective-C Declaration
```objective-c
+ (instancetype)storeWithURLAndLegacyFilename:(NSURL *)url;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に `API::ContentRuleListStore::storeWithPath(url.absoluteURL.path)` を呼び、ラッパーを `autorelease` して返す。無効時は `nil`。レガシーファイル名の扱いは下位実装に委ねられる。

## References
- [`WKContentRuleListStorePrivate.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L40)
- [`WKContentRuleListStore.mm#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L238)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
