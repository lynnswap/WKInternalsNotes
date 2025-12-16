# ``WKInternalsNotes/WKPreferencesPrivate/_wantsBalancedSetDefersLoadingBehavior``

Balanced Set Defers Loading Behavior を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setWantsBalancedSetDefersLoadingBehavior:) BOOL _wantsBalancedSetDefersLoadingBehavior WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_wantsBalancedSetDefersLoadingBehavior = YES`: Balanced Set Defers Loading Behavior を有効化する。
- `_wantsBalancedSetDefersLoadingBehavior = NO`: Balanced Set Defers Loading Behavior を無効化する。
- Implementation: [`Source/WebCore/page/Page.cpp#L1592`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp#L1592) の `Page::setDefersLoading` が `wantsBalancedSetDefersLoadingBehavior()` を参照する。

## Details
- WebPreferences key: `WantsBalancedSetDefersLoadingBehavior`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L238)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1319`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1319)
- [`Source/WebCore/page/Page.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8806`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8806) (key: `WantsBalancedSetDefersLoadingBehavior`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
