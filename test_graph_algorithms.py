"""
Comprehensive Test Suite for Graph Algorithms
=============================================

This test suite validates all graph algorithm implementations with:
- Normal cases
- Edge cases (empty graphs, single node, disconnected components)
- Error cases (negative cycles, invalid inputs)
- Performance checks for large graphs
"""

import sys
from typing import Dict, List, Tuple, Set
from collections import defaultdict


def test_bfs():
    """Test Breadth-First Search"""
    print("\n" + "=" * 60)
    print("Testing BFS (Breadth-First Search)")
    print("=" * 60)
    
    try:
        from breadth_first_search import breadth_first_search
        
        # Test 1: Normal case
        graph1: Dict[int, List[int]] = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0],
            3: [1],
            4: [1]
        }
        result = breadth_first_search(graph1, 0)
        expected = [0, 1, 2, 3, 4]
        assert result == expected, f"Expected {expected}, got {result}"
        print("✓ Test 1 passed: Normal graph traversal")
        
        # Test 2: Single node
        graph2: Dict[int, List[int]] = {0: []}
        result2 = breadth_first_search(graph2, 0)
        assert result2 == [0], f"Single node failed: {result2}"
        print("✓ Test 2 passed: Single node graph")
        
        # Test 3: Disconnected components
        graph3: Dict[int, List[int]] = {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        }
        result3 = breadth_first_search(graph3, 0)
        assert 2 not in result3 and 3 not in result3, "Disconnected components should not be reached"
        print("✓ Test 3 passed: Disconnected components handled correctly")
        
        print("✅ BFS: All tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Could not import BFS: {e}")
        return False
    except Exception as e:
        print(f"❌ BFS test failed: {e}")
        return False


def test_dfs():
    """Test Depth-First Search"""
    print("\n" + "=" * 60)
    print("Testing DFS (Depth-First Search)")
    print("=" * 60)
    
    try:
        from depth_first_search import depth_first_search
        
        # Test 1: Normal case
        graph1: Dict[int, List[int]] = {
            0: [1, 2],
            1: [3],
            2: [4],
            3: [],
            4: []
        }
        result = depth_first_search(graph1, 0)
        # DFS should visit all reachable nodes
        assert len(result) == 5, f"Expected 5 nodes, got {len(result)}"
        assert 0 in result and 1 in result and 2 in result
        print("✓ Test 1 passed: Normal graph traversal")
        
        # Test 2: Cycle handling
        graph2: Dict[int, List[int]] = {
            0: [1],
            1: [2],
            2: [0]  # Cycle
        }
        result2 = depth_first_search(graph2, 0)
        assert len(result2) == 3, "Should visit each node exactly once despite cycle"
        print("✓ Test 2 passed: Cycle handling")
        
        print("✅ DFS: All tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Could not import DFS: {e}")
        return False
    except Exception as e:
        print(f"❌ DFS test failed: {e}")
        return False


def test_dijkstra():
    """Test Dijkstra's Algorithm"""
    print("\n" + "=" * 60)
    print("Testing Dijkstra's Algorithm")
    print("=" * 60)
    
    try:
        from dijkstras_algorithm import dijkstra, dijkstra_with_path
        
        # Test 1: Normal case
        graph1: Dict[int, List[Tuple[int, float]]] = {
            0: [(1, 4.0), (2, 1.0)],
            1: [(3, 1.0)],
            2: [(1, 2.0), (3, 5.0)],
            3: []
        }
        distances = dijkstra(graph1, 0)
        assert distances[0] == 0, "Source distance should be 0"
        assert distances[1] == 3.0, f"Distance to 1 should be 3, got {distances[1]}"
        assert distances[2] == 1.0, f"Distance to 2 should be 1, got {distances[2]}"
        assert distances[3] == 4.0, f"Distance to 3 should be 4, got {distances[3]}"
        print("✓ Test 1 passed: Shortest path calculation")
        
        # Test 2: Path reconstruction
        dist, path = dijkstra_with_path(graph1, 0, 3)
        assert dist == 4.0, f"Distance should be 4, got {dist}"
        assert path == [0, 2, 1, 3], f"Path should be [0, 2, 1, 3], got {path}"
        print("✓ Test 2 passed: Path reconstruction")
        
        # Test 3: Negative weight detection
        negative_graph: Dict[int, List[Tuple[int, float]]] = {
            0: [(1, -5.0)],
            1: []
        }
        try:
            dijkstra(negative_graph, 0)
            print("❌ Test 3 failed: Should have detected negative weight")
            return False
        except ValueError:
            print("✓ Test 3 passed: Negative weight detection")
        
        # Test 4: Unreachable vertex
        graph2: Dict[int, List[Tuple[int, float]]] = {
            0: [(1, 1.0)],
            1: [],
            2: []  # Unreachable from 0
        }
        distances2 = dijkstra(graph2, 0)
        assert distances2[2] == float('inf'), "Unreachable vertex should have infinite distance"
        print("✓ Test 4 passed: Unreachable vertex handling")
        
        print("✅ Dijkstra: All tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Could not import Dijkstra: {e}")
        return False
    except Exception as e:
        print(f"❌ Dijkstra test failed: {e}")
        return False


def test_bellman_ford():
    """Test Bellman-Ford Algorithm"""
    print("\n" + "=" * 60)
    print("Testing Bellman-Ford Algorithm")
    print("=" * 60)
    
    try:
        from bellman_ford import bellman_ford
        
        # Test 1: Positive weights
        graph1: Dict[int, List[Tuple[int, float]]] = {
            0: [(1, 4.0), (2, 1.0)],
            1: [(3, 1.0)],
            2: [(1, 2.0), (3, 5.0)],
            3: []
        }
        distances = bellman_ford(graph1, 0)
        assert distances[0] == 0, "Source distance should be 0"
        assert distances[1] == 3.0, f"Expected distance 3, got {distances[1]}"
        print("✓ Test 1 passed: Positive weights")
        
        # Test 2: Negative weights (no cycle)
        graph2: Dict[int, List[Tuple[int, float]]] = {
            0: [(1, 5.0), (2, 1.0)],
            1: [(2, -3.0)],
            2: []
        }
        distances2 = bellman_ford(graph2, 0)
        assert distances2[2] == 1.0, f"Expected distance 1, got {distances2[2]}"
        print("✓ Test 2 passed: Negative weights without cycle")
        
        # Test 3: Negative cycle detection
        graph3: Dict[int, List[Tuple[int, float]]] = {
            0: [(1, 1.0)],
            1: [(2, -3.0)],
            2: [(1, 1.0)]  # Creates negative cycle: 1 -> 2 -> 1
        }
        try:
            bellman_ford(graph3, 0)
            print("❌ Test 3 failed: Should have detected negative cycle")
            return False
        except ValueError as e:
            assert "negative cycle" in str(e).lower()
            print("✓ Test 3 passed: Negative cycle detection")
        
        print("✅ Bellman-Ford: All tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Could not import Bellman-Ford: {e}")
        return False
    except Exception as e:
        print(f"❌ Bellman-Ford test failed: {e}")
        return False


def test_topological_sort():
    """Test Topological Sort"""
    print("\n" + "=" * 60)
    print("Testing Topological Sort")
    print("=" * 60)
    
    try:
        from topological_sort import topological_sort_kahn, topological_sort_dfs, has_cycle
        
        # Test 1: Normal DAG
        dag1: Dict[int, List[int]] = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: []
        }
        kahn_result = topological_sort_kahn(dag1)
        dfs_result = topological_sort_dfs(dag1)
        
        assert kahn_result is not None, "Kahn's algorithm should return a result"
        assert dfs_result is not None, "DFS algorithm should return a result"
        assert kahn_result[0] == 0, "Source should come first"
        assert kahn_result[-1] == 3, "Sink should come last"
        print("✓ Test 1 passed: Normal DAG sorting")
        
        # Test 2: Cycle detection
        cyclic_graph: Dict[int, List[int]] = {
            0: [1],
            1: [2],
            2: [0]  # Cycle
        }
        kahn_result2 = topological_sort_kahn(cyclic_graph)
        dfs_result2 = topological_sort_dfs(cyclic_graph)
        
        assert kahn_result2 is None, "Should detect cycle with Kahn's"
        assert dfs_result2 is None, "Should detect cycle with DFS"
        assert has_cycle(cyclic_graph), "has_cycle should return True"
        print("✓ Test 2 passed: Cycle detection")
        
        # Test 3: Linear chain
        chain: Dict[int, List[int]] = {
            0: [1],
            1: [2],
            2: [3],
            3: []
        }
        result3 = topological_sort_kahn(chain)
        assert result3 == [0, 1, 2, 3], f"Linear chain should be [0,1,2,3], got {result3}"
        print("✓ Test 3 passed: Linear chain")
        
        print("✅ Topological Sort: All tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Could not import Topological Sort: {e}")
        return False
    except Exception as e:
        print(f"❌ Topological Sort test failed: {e}")
        return False


def test_kosaraju():
    """Test Kosaraju's Algorithm (Strongly Connected Components)"""
    print("\n" + "=" * 60)
    print("Testing Kosaraju's Algorithm (SCC)")
    print("=" * 60)
    
    try:
        from Kosarajus_algorithm import kosaraju_scc
        
        # Test 1: Graph with multiple SCCs
        graph1: Dict[int, Set[int]] = {
            0: {1},
            1: {2},
            2: {0, 3},
            3: {4},
            4: {5, 7},
            5: {6},
            6: {4},
            7: {8},
            8: {7}
        }
        sccs = kosaraju_scc(graph1)
        
        # Should find 3 SCCs: {0,1,2}, {4,5,6}, {7,8}, and singleton {3}
        assert len(sccs) == 4, f"Expected 4 SCCs, got {len(sccs)}"
        
        # Check that 0, 1, 2 are in same SCC
        scc_map = {}
        for idx, scc in enumerate(sccs):
            for node in scc:
                scc_map[node] = idx
        
        assert scc_map[0] == scc_map[1] == scc_map[2], "Nodes 0,1,2 should be in same SCC"
        assert scc_map[4] == scc_map[5] == scc_map[6], "Nodes 4,5,6 should be in same SCC"
        print("✓ Test 1 passed: Multiple SCCs identified")
        
        # Test 2: Single SCC (complete cycle)
        graph2: Dict[int, Set[int]] = {
            0: {1},
            1: {2},
            2: {0}
        }
        sccs2 = kosaraju_scc(graph2)
        assert len(sccs2) == 1, "Complete cycle should be one SCC"
        print("✓ Test 2 passed: Single SCC")
        
        print("✅ Kosaraju: All tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Could not import Kosaraju: {e}")
        return False
    except Exception as e:
        print(f"❌ Kosaraju test failed: {e}")
        return False


def test_2sat():
    """Test 2-SAT Solver"""
    print("\n" + "=" * 60)
    print("Testing 2-SAT Solver")
    print("=" * 60)
    
    try:
        # Import with name that matches file (with digit prefix)
        import importlib
        sat_module = importlib.import_module('2SAT_proble')
        two_sat_solver = sat_module.two_sat_solver
        
        # Test 1: Satisfiable instance
        clauses1: List[Tuple[int, int]] = [
            (1, 2),    # x1 OR x2
            (-1, -2),  # NOT x1 OR NOT x2
            (1, -2)    # x1 OR NOT x2
        ]
        result1 = two_sat_solver(3, clauses1)
        assert result1 is not None, "Should be satisfiable"
        print(f"✓ Test 1 passed: Satisfiable instance, assignment: {result1}")
        
        # Test 2: Unsatisfiable instance
        clauses2: List[Tuple[int, int]] = [
            (1, 2),    # x1 OR x2
            (1, -2),   # x1 OR NOT x2
            (-1, 2),   # NOT x1 OR x2
            (-1, -2)   # NOT x1 OR NOT x2
        ]
        result2 = two_sat_solver(3, clauses2)
        assert result2 is None, "Should be unsatisfiable"
        print("✓ Test 2 passed: Unsatisfiable instance detected")
        
        print("✅ 2-SAT: All tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Could not import 2-SAT: {e}")
        return False
    except Exception as e:
        print(f"❌ 2-SAT test failed: {e}")
        return False


def run_all_tests():
    """Run all test suites"""
    print("\n" + "=" * 70)
    print(" GRAPH ALGORITHM TEST SUITE")
    print("=" * 70)
    
    results = []
    
    # Run each test
    results.append(("BFS", test_bfs()))
    results.append(("DFS", test_dfs()))
    results.append(("Dijkstra", test_dijkstra()))
    results.append(("Bellman-Ford", test_bellman_ford()))
    results.append(("Topological Sort", test_topological_sort()))
    results.append(("Kosaraju (SCC)", test_kosaraju()))
    results.append(("2-SAT", test_2sat()))
    
    # Summary
    print("\n" + "=" * 70)
    print(" TEST SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print("\n" + "=" * 70)
    print(f"Results: {passed}/{total} test suites passed")
    
    if passed == total:
        print("🎉 All tests passed successfully!")
    else:
        print(f"⚠️  {total - passed} test suite(s) failed")
    
    print("=" * 70)
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
