# ``WKInternalsNotes/WKWebpagePreferences/_setContentRuleListsEnabled(_:exceptions:)``

Content Rule List の既定有効/無効と例外を設定する。

## Objective-C Declaration
```objective-c
- (void)_setContentRuleListsEnabled:(BOOL)enabled exceptions:(NSSet<NSString *> *)exceptions WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
例外 identifier を `HashSet<String>` に変換し、`setContentExtensionEnablement` に既定値と例外セットを渡して設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L130)
- [`WKWebpagePreferences.mm#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L214)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
