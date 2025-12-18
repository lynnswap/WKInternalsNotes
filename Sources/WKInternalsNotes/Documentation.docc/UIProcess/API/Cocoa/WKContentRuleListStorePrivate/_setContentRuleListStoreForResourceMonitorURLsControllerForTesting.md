# ``WKInternalsNotes/WKContentRuleListStore/_setContentRuleListStoreForResourceMonitorURLsControllerForTesting(_:)``

ResourceMonitorURLsController の content rule list store をテスト用に差し替える。

## Objective-C Declaration
```objective-c
+ (void)_setContentRuleListStoreForResourceMonitorURLsControllerForTesting:(WKContentRuleListStore *)store;
```

## Discussion
`ENABLE(ADVANCED_PRIVACY_PROTECTIONS)` の場合に `store->_contentRuleListStore` から `API::ContentRuleListStore` を取り出し、`ResourceMonitorURLsController::singleton().setContentRuleListStore` に渡す。無効時は `UNUSED_PARAM(store)` で何もしない。

## References
- [`WKContentRuleListStorePrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L37)
- [`WKContentRuleListStore.mm#L218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L218)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
